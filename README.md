# Build Analyzer Script

This Python script analyzes VC build logs to extract commit information and dependent components, following the dependency chain through multiple build logs.

## Overview

The script performs the following analysis workflow:

1. **Analyze VC build** - Downloads and parses the main VC build log to extract:
   - Commit hash (changenumber)
   - Dependent component build numbers (cayman_stateless_photon, wcp)

2. **Analyze cayman_stateless_photon** - Downloads and parses the photon build log to extract:
   - Commit hash (changenumber)
   - NSX-UJO dependency build number

3. **Analyze WCP** - Downloads and parses the WCP build log to extract:
   - Commit hash (changenumber)
   - NSX-UJO dependency build number

4. **Analyze NSX-UJO builds** - Downloads and parses NSX-UJO build logs to extract:
   - NSX-Operator commit hash from git clone/reset commands

5. **Generate output table** - Creates a formatted table with build numbers and commit page URLs

## Files

- `build_analyzer.py` - Main script implementation
- `test_build_analyzer.py` - Test script with mock data
- `README.md` - This documentation file

## Usage

```bash
python build_analyzer.py <vc_build_number>
```

### Example

```bash
python build_analyzer.py 24812785
```

This will analyze VC build `ob-24812785` and output a table like:

```
================================================================================
Component            Build Number         Commit Page
================================================================================
vc                   ob-24812785          https://github-vcf.devops.broadcom.net/vcf/tera/commit/c9d4707896b697492b8300b7645673d29b4ccb36
wcp                  ob-24799010          https://github-vcf.devops.broadcom.net/vcf/tera/commit/ea595ce2ea172f1226a4ed105803a9207e179e06
photon               ob-24804127          https://github-vcf.devops.broadcom.net/vcf/cayman_photon/commit/ed495259f2296f640de97f7f18ed7f2f61bee6a9
wcp/nsx-ujo          ob-24793041          N/A
photon/nsx-ujo       ob-24793041          N/A
wcp/nsx-operator     ob-24793041          https://gitlab-vmw.devops.broadcom.net/core-build/mirrors_github_nsx-operator/-/commit/6b6b9464dc435af5dceb891ca8f238903d19cef5
photon/nsx-operator  ob-24793041          https://gitlab-vmw.devops.broadcom.net/core-build/mirrors_github_nsx-operator/-/commit/6b6b9464dc435af5dceb891ca8f238903d19cef5
================================================================================
```

## Dependencies

The script uses existing project modules:
- `logger.py` - For logging functionality
- `util.py` - For command execution utilities

Standard Python libraries used:
- `re` - Regular expressions for log parsing
- `os`, `sys` - System operations
- `tempfile` - Temporary file handling
- `urllib.parse` - URL parsing

## Testing

Run the test script to verify functionality:

```bash
python test_build_analyzer.py
```

The test script uses mock data to validate:
- Log parsing functions
- URL generation for different repositories
- Results table formatting

## Implementation Details

### BuildAnalyzer Class

The main `BuildAnalyzer` class provides the following methods:

- `download_log(build_number, log_type)` - Downloads build logs using wget
- `parse_vc_log(log_file)` - Parses VC build logs to extract commit and dependencies
- `parse_component_log(log_file, component_name)` - Parses component logs (photon/wcp)
- `parse_nsx_ujo_log(log_file)` - Extracts NSX-Operator commit from NSX-UJO logs
- `get_commit_page_url(repo, commit)` - Generates commit page URLs for different repositories
- `analyze_build(vc_build_number)` - Main analysis workflow
- `print_results_table(results)` - Formats and prints the results table

### URL Generation

The script generates commit page URLs for different repository types:
- **GitHub VCF repositories** (tera, cayman_photon): `https://github-vcf.devops.broadcom.net/vcf/{repo}/commit/{commit}`
- **GitLab repositories** (nsx-operator): `https://gitlab-vmw.devops.broadcom.net/core-build/mirrors_github_nsx-operator/-/commit/{commit}`

### Error Handling

The script includes error handling for:
- Failed log downloads
- Missing commit information
- Missing dependency information
- File I/O errors

## Network Requirements

The script requires network access to:
- `https://build-squid.vcfd.broadcom.net` - For downloading build logs
- External wget command functionality

## Limitations

- Requires access to internal Broadcom build infrastructure
- Depends on specific log format patterns
- Uses temporary files in `/tmp/` directory
- Requires wget command to be available in the system PATH