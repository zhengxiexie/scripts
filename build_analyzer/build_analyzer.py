#!/usr/bin/env python3

import re
import sys

from util import util
from util.logger import get_logger

log = get_logger(__name__)

class BuildAnalyzer:
    def __init__(self):
        self.base_url = "https://build-squid.vcfd.broadcom.net/build/mts/release"
        self.github_vcf_base = "https://github-vcf.devops.broadcom.net/vcf"
        self.gitlab_base = "https://gitlab-vmw.devops.broadcom.net/core-build/mirrors_github_nsx-operator"

    def parse_build_number(self, build_input):
        """Parse build input to extract build type and number"""
        if build_input.startswith('ob-'):
            return 'ob', build_input[3:]
        elif build_input.startswith('sb-'):
            return 'sb', build_input[3:]
        else:
            # Default to ob if no prefix is provided
            return 'ob', build_input

    def download_log(self, build_number, build_type='ob', log_type="gobuilds.log"):
        """Download build log for given build number and type"""
        if build_type == 'ob':
            url = f"{self.base_url}/bora-{build_number}/logs/linux-rocky8-vm-fw/{log_type}"
        else:  # sb
            url = f"{self.base_url}/sb-{build_number}/logs/linux-rocky8-vm-fw/{log_type}"

        temp_file = f"/tmp/build_{build_type}_{build_number}_{log_type}"

        log.info(f"Downloading log from {url}")
        ret_code, output = util.runcmd(f"wget -q -O {temp_file} {url}")

        if ret_code != 0:
            log.error(f"Failed to download log: {output}")
            return None

        return temp_file

    def parse_vc_log(self, log_file):
        """Parse VC build log to extract commit, branch and dependencies"""
        log.info(f"Parsing VC log: {log_file}")

        with open(log_file, 'r') as f:
            content = f.read()

        # Extract changenumber (commit)
        commit_match = re.search(r'--changenumber=([a-f0-9]{40})', content)
        commit = commit_match.group(1) if commit_match else None

        # Extract branch
        branch_match = re.search(r'--branch=([^\s]+)', content)
        branch = branch_match.group(1) if branch_match else None

        # Extract dependent components (support both ob- and sb- prefixes)
        cayman_match = re.search(r'cayman_stateless_photon=(ob|sb)-(\d+)', content)
        wcp_match = re.search(r'wcp=(ob|sb)-(\d+)', content)

        cayman_build = None
        cayman_type = None
        if cayman_match:
            cayman_type = cayman_match.group(1)
            cayman_build = cayman_match.group(2)

        wcp_build = None
        wcp_type = None
        if wcp_match:
            wcp_type = wcp_match.group(1)
            wcp_build = wcp_match.group(2)

        return {
            'commit': commit,
            'branch': branch,
            'cayman_stateless_photon': cayman_build,
            'cayman_type': cayman_type,
            'wcp': wcp_build,
            'wcp_type': wcp_type
        }

    def parse_component_log(self, log_file, component_name):
        """Parse component log (cayman_stateless_photon or wcp) to extract commit, branch and nsx-ujo dependency"""
        log.info(f"Parsing {component_name} log: {log_file}")

        with open(log_file, 'r') as f:
            content = f.read()

        # Extract changenumber (commit)
        commit_match = re.search(r'--changenumber=([a-f0-9]{40})', content)
        commit = commit_match.group(1) if commit_match else None

        # Extract branch
        branch_match = re.search(r'--branch=([^\s]+)', content)
        branch = branch_match.group(1) if branch_match else None

        # Extract nsx-ujo dependency (support both ob- and sb- prefixes)
        nsx_ujo_match = re.search(r'nsx-ujo=(ob|sb)-(\d+)', content)
        nsx_ujo_build = None
        nsx_ujo_type = None
        if nsx_ujo_match:
            nsx_ujo_type = nsx_ujo_match.group(1)
            nsx_ujo_build = nsx_ujo_match.group(2)

        return {
            'commit': commit,
            'branch': branch,
            'nsx_ujo': nsx_ujo_build,
            'nsx_ujo_type': nsx_ujo_type
        }

    def parse_nsx_ujo_log(self, log_file):
        """Parse nsx-ujo log to extract nsx-ujo commit, branch and nsx-operator commit"""
        log.info(f"Parsing nsx-ujo log: {log_file}")

        with open(log_file, 'r') as f:
            content = f.read()

        # Extract nsx-ujo changenumber (commit)
        commit_match = re.search(r'--changenumber=([a-f0-9]{40})', content)
        nsx_ujo_commit = commit_match.group(1) if commit_match else None

        # Extract branch
        branch_match = re.search(r'--branch=([^\s]+)', content)
        nsx_ujo_branch = branch_match.group(1) if branch_match else None

        # Look for the git clone and reset pattern for nsx-operator
        pattern = r'git clone.*nsx-operator.*head_commit_id=([a-f0-9]{40}).*git reset ([a-f0-9]{40})'
        match = re.search(pattern, content, re.DOTALL)

        nsx_operator_commit = None
        if match:
            commit_id = match.group(1)
            reset_id = match.group(2)
            # They should be the same, use the reset_id as it's the final commit
            nsx_operator_commit = reset_id
        else:
            # Alternative pattern if the format is different
            alt_pattern = r'head_commit_id=([a-f0-9]{40})'
            alt_match = re.search(alt_pattern, content)
            if alt_match:
                nsx_operator_commit = alt_match.group(1)

        return {
            'nsx_ujo_commit': nsx_ujo_commit,
            'nsx_ujo_branch': nsx_ujo_branch,
            'nsx_operator_commit': nsx_operator_commit
        }

    def get_commit_page_url(self, repo, commit):
        """Generate commit page URL"""
        if repo == 'nsx-operator':
            return f"{self.gitlab_base}/-/commit/{commit}"
        else:
            return f"{self.github_vcf_base}/{repo}/commit/{commit}"

    def analyze_build(self, vc_build_input):
        """Main analysis function"""
        # Parse the build input to get type and number
        vc_build_type, vc_build_number = self.parse_build_number(vc_build_input)
        log.info(f"Starting analysis for VC build: {vc_build_type}-{vc_build_number}")

        results = {}

        # Step 1: Analyze VC build
        vc_log = self.download_log(vc_build_number, vc_build_type)
        if not vc_log:
            log.error("Failed to download VC log")
            return None

        vc_data = self.parse_vc_log(vc_log)
        results['vc'] = {
            'build_number': f"{vc_build_type}-{vc_build_number}",
            'branch': vc_data['branch'] if vc_data['branch'] else 'N/A',
            'commit_page': self.get_commit_page_url('tera', vc_data['commit']) if vc_data['commit'] else 'N/A'
        }

        # Step 2: Analyze cayman_stateless_photon
        if vc_data['cayman_stateless_photon']:
            photon_build_type = vc_data['cayman_type'] or 'ob'
            photon_log = self.download_log(vc_data['cayman_stateless_photon'], photon_build_type)
            if photon_log:
                photon_data = self.parse_component_log(photon_log, 'cayman_stateless_photon')
                results['photon'] = {
                    'build_number': f"{photon_build_type}-{vc_data['cayman_stateless_photon']}",
                    'branch': photon_data['branch'] if photon_data['branch'] else 'N/A',
                    'commit_page': self.get_commit_page_url('cayman_photon', photon_data['commit']) if photon_data['commit'] else 'N/A'
                }

                # Step 3: Analyze photon's nsx-ujo
                if photon_data['nsx_ujo']:
                    photon_nsx_build_type = photon_data['nsx_ujo_type'] or 'ob'
                    photon_nsx_log = self.download_log(photon_data['nsx_ujo'], photon_nsx_build_type)
                    if photon_nsx_log:
                        photon_nsx_data = self.parse_nsx_ujo_log(photon_nsx_log)
                        results['photon/nsx-ujo'] = {
                            'build_number': f"{photon_nsx_build_type}-{photon_data['nsx_ujo']}",
                            'branch': photon_nsx_data['nsx_ujo_branch'] if photon_nsx_data['nsx_ujo_branch'] else 'N/A',
                            'commit_page': self.get_commit_page_url('nsx-ujo', photon_nsx_data['nsx_ujo_commit']) if photon_nsx_data['nsx_ujo_commit'] else 'N/A'
                        }
                        results['photon/nsx-operator'] = {
                            'build_number': f"N/A",
                            'branch': 'N/A',
                            'commit_page': self.get_commit_page_url('nsx-operator', photon_nsx_data['nsx_operator_commit']) if photon_nsx_data['nsx_operator_commit'] else 'N/A'
                        }

        # Step 4: Analyze wcp
        if vc_data['wcp']:
            wcp_build_type = vc_data['wcp_type'] or 'ob'
            wcp_log = self.download_log(vc_data['wcp'], wcp_build_type)
            if wcp_log:
                wcp_data = self.parse_component_log(wcp_log, 'wcp')
                results['wcp'] = {
                    'build_number': f"{wcp_build_type}-{vc_data['wcp']}",
                    'branch': wcp_data['branch'] if wcp_data['branch'] else 'N/A',
                    'commit_page': self.get_commit_page_url('tera', wcp_data['commit']) if wcp_data['commit'] else 'N/A'
                }

                # Step 5: Analyze wcp's nsx-ujo
                if wcp_data['nsx_ujo']:
                    wcp_nsx_build_type = wcp_data['nsx_ujo_type'] or 'ob'
                    wcp_nsx_log = self.download_log(wcp_data['nsx_ujo'], wcp_nsx_build_type)
                    if wcp_nsx_log:
                        wcp_nsx_data = self.parse_nsx_ujo_log(wcp_nsx_log)
                        results['wcp/nsx-ujo'] = {
                            'build_number': f"{wcp_nsx_build_type}-{wcp_data['nsx_ujo']}",
                            'branch': wcp_nsx_data['nsx_ujo_branch'] if wcp_nsx_data['nsx_ujo_branch'] else 'N/A',
                            'commit_page': self.get_commit_page_url('nsx-ujo', wcp_nsx_data['nsx_ujo_commit']) if wcp_nsx_data['nsx_ujo_commit'] else 'N/A'
                        }
                        results['wcp/nsx-operator'] = {
                            'build_number': f"N/A",
                            'branch': 'N/A',
                            'commit_page': self.get_commit_page_url('nsx-operator', wcp_nsx_data['nsx_operator_commit']) if wcp_nsx_data['nsx_operator_commit'] else 'N/A'
                        }

        return results

    def analyze_wcp_build(self, wcp_build_input):
        """Analyze WCP build only (without vc and photon)"""
        # Parse the build input to get type and number
        wcp_build_type, wcp_build_number = self.parse_build_number(wcp_build_input)
        log.info(f"Starting WCP analysis for build: {wcp_build_type}-{wcp_build_number}")

        results = {}

        # Analyze WCP build
        wcp_log = self.download_log(wcp_build_number, wcp_build_type)
        if not wcp_log:
            log.error("Failed to download WCP log")
            return None

        wcp_data = self.parse_component_log(wcp_log, 'wcp')
        results['wcp'] = {
            'build_number': f"{wcp_build_type}-{wcp_build_number}",
            'branch': wcp_data['branch'] if wcp_data['branch'] else 'N/A',
            'commit_page': self.get_commit_page_url('tera', wcp_data['commit']) if wcp_data['commit'] else 'N/A'
        }

        # Analyze wcp's nsx-ujo
        if wcp_data['nsx_ujo']:
            wcp_nsx_build_type = wcp_data['nsx_ujo_type'] or 'ob'
            wcp_nsx_log = self.download_log(wcp_data['nsx_ujo'], wcp_nsx_build_type)
            if wcp_nsx_log:
                wcp_nsx_data = self.parse_nsx_ujo_log(wcp_nsx_log)
                results['wcp/nsx-ujo'] = {
                    'build_number': f"{wcp_nsx_build_type}-{wcp_data['nsx_ujo']}",
                    'branch': wcp_nsx_data['nsx_ujo_branch'] if wcp_nsx_data['nsx_ujo_branch'] else 'N/A',
                    'commit_page': self.get_commit_page_url('nsx-ujo', wcp_nsx_data['nsx_ujo_commit']) if wcp_nsx_data['nsx_ujo_commit'] else 'N/A'
                }
                results['wcp/nsx-operator'] = {
                    'build_number': f"N/A",
                    'branch': 'N/A',
                    'commit_page': self.get_commit_page_url('nsx-operator', wcp_nsx_data['nsx_operator_commit']) if wcp_nsx_data['nsx_operator_commit'] else 'N/A'
                }

        return results

    def analyze_photon_build(self, photon_build_input):
        """Analyze photon build only (without vc and wcp)"""
        # Parse the build input to get type and number
        photon_build_type, photon_build_number = self.parse_build_number(photon_build_input)
        log.info(f"Starting photon analysis for build: {photon_build_type}-{photon_build_number}")

        results = {}

        # Analyze photon build
        photon_log = self.download_log(photon_build_number, photon_build_type)
        if not photon_log:
            log.error("Failed to download photon log")
            return None

        photon_data = self.parse_component_log(photon_log, 'cayman_stateless_photon')
        results['photon'] = {
            'build_number': f"{photon_build_type}-{photon_build_number}",
            'branch': photon_data['branch'] if photon_data['branch'] else 'N/A',
            'commit_page': self.get_commit_page_url('cayman_photon', photon_data['commit']) if photon_data['commit'] else 'N/A'
        }

        # Analyze photon's nsx-ujo
        if photon_data['nsx_ujo']:
            photon_nsx_build_type = photon_data['nsx_ujo_type'] or 'ob'
            photon_nsx_log = self.download_log(photon_data['nsx_ujo'], photon_nsx_build_type)
            if photon_nsx_log:
                photon_nsx_data = self.parse_nsx_ujo_log(photon_nsx_log)
                results['photon/nsx-ujo'] = {
                    'build_number': f"{photon_nsx_build_type}-{photon_data['nsx_ujo']}",
                    'branch': photon_nsx_data['nsx_ujo_branch'] if photon_nsx_data['nsx_ujo_branch'] else 'N/A',
                    'commit_page': self.get_commit_page_url('nsx-ujo', photon_nsx_data['nsx_ujo_commit']) if photon_nsx_data['nsx_ujo_commit'] else 'N/A'
                }
                results['photon/nsx-operator'] = {
                    'build_number': f"N/A",
                    'branch': 'N/A',
                    'commit_page': self.get_commit_page_url('nsx-operator', photon_nsx_data['nsx_operator_commit']) if photon_nsx_data['nsx_operator_commit'] else 'N/A'
                }

        return results

    def analyze_nsx_ujo_build(self, nsx_ujo_build_input):
        """Analyze nsx-ujo build only (without vc, wcp, and photon)"""
        # Parse the build input to get type and number
        nsx_ujo_build_type, nsx_ujo_build_number = self.parse_build_number(nsx_ujo_build_input)
        log.info(f"Starting nsx-ujo analysis for build: {nsx_ujo_build_type}-{nsx_ujo_build_number}")

        results = {}

        # Analyze nsx-ujo build
        nsx_ujo_log = self.download_log(nsx_ujo_build_number, nsx_ujo_build_type)
        if not nsx_ujo_log:
            log.error("Failed to download nsx-ujo log")
            return None

        nsx_ujo_data = self.parse_nsx_ujo_log(nsx_ujo_log)
        results['nsx-ujo'] = {
            'build_number': f"{nsx_ujo_build_type}-{nsx_ujo_build_number}",
            'branch': nsx_ujo_data['nsx_ujo_branch'] if nsx_ujo_data['nsx_ujo_branch'] else 'N/A',
            'commit_page': self.get_commit_page_url('nsx-ujo', nsx_ujo_data['nsx_ujo_commit']) if nsx_ujo_data['nsx_ujo_commit'] else 'N/A'
        }
        results['nsx-operator'] = {
            'build_number': f"N/A",
            'branch': 'N/A',
            'commit_page': self.get_commit_page_url('nsx-operator', nsx_ujo_data['nsx_operator_commit']) if nsx_ujo_data['nsx_operator_commit'] else 'N/A'
        }

        return results

    def print_results_table(self, results, start_component='vc'):
        """Print results in table format"""
        print("\n" + "="*100)
        print(f"{'Component':<20} {'Build Number':<20} {'Branch':<15} {'Commit Page'}")
        print("="*100)

        # Define component sets based on starting component
        if start_component == 'vc':
            components = ['vc', 'wcp', 'photon', 'wcp/nsx-ujo', 'photon/nsx-ujo', 'wcp/nsx-operator', 'photon/nsx-operator']
        elif start_component == 'wcp':
            components = ['wcp', 'wcp/nsx-ujo', 'wcp/nsx-operator']
        elif start_component == 'photon':
            components = ['photon', 'photon/nsx-ujo', 'photon/nsx-operator']
        elif start_component == 'nsx-ujo':
            components = ['nsx-ujo', 'nsx-operator']
        else:
            # Default to all components
            components = ['vc', 'wcp', 'photon', 'wcp/nsx-ujo', 'photon/nsx-ujo', 'wcp/nsx-operator', 'photon/nsx-operator']

        for component in components:
            if component in results:
                build_num = results[component]['build_number']
                branch = results[component]['branch']
                commit_page = results[component]['commit_page']
                print(f"{component:<20} {build_num:<20} {branch:<15} {commit_page}")
            else:
                print(f"{component:<20} {'N/A':<20} {'N/A':<15} {'N/A'}")

        print("="*100)

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python build_analyzer.py [<component>] <build_number>")
        print("Examples:")
        print("  python build_analyzer.py 24812785           # defaults to vc ob-24812785")
        print("  python build_analyzer.py vc sb-87632192     # analyze from VC")
        print("  python build_analyzer.py wcp ob-24838365    # analyze from WCP only")
        print("  python build_analyzer.py nsx-ujo ob-24832036 # analyze from NSX-UJO only")
        print("  python build_analyzer.py photon sb-87616055 # analyze from photon only")
        sys.exit(1)

    analyzer = BuildAnalyzer()

    # Handle different argument patterns
    if len(sys.argv) == 2:
        # Old format: python build_analyzer.py <build_number>
        # Default to VC analysis
        component = 'vc'
        build_input = sys.argv[1]
    else:
        # New format: python build_analyzer.py <component> <build_number>
        component = sys.argv[1].lower()
        build_input = sys.argv[2]

    # Validate component type
    valid_components = ['vc', 'wcp', 'nsx-ujo', 'photon']
    if component not in valid_components:
        print(f"Error: Invalid component '{component}'. Valid components are: {', '.join(valid_components)}")
        sys.exit(1)

    # Analyze based on component type
    if component == 'vc':
        results = analyzer.analyze_build(build_input)
    elif component == 'wcp':
        results = analyzer.analyze_wcp_build(build_input)
    elif component == 'nsx-ujo':
        results = analyzer.analyze_nsx_ujo_build(build_input)
    elif component == 'photon':
        results = analyzer.analyze_photon_build(build_input)

    if results:
        analyzer.print_results_table(results, component)
    else:
        log.error("Analysis failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
