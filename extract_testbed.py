import os
import re

import requests
import json
import subprocess


def download_json(url, filename):
    if os.path.exists(filename):
        print(f"Loading data from {filename}")
        with open(filename, 'r') as file:
            return json.load(file)

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Save the JSON to a file
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

        return data
    except requests.RequestException as e:
        print(f"ERROR: Failed to download JSON from {url} - {e}")
        return None


def execute_remote_command(ip, username, root_password, password, command):
    try:
        result = subprocess.run(
            ['sshpass', '-p', root_password, '/usr/bin/ssh',
             '-o', 'StrictHostKeyChecking=no',
             '-o', 'UserKnownHostsFile=/dev/null',
             f"{username}@{ip}", command],
            capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Command execution failed: {e}")
        return None


def get_api_servers(vc_ip, username, root_password, vc_password):
    dcli_command = (
        f"dcli +username 'administrator@vsphere.local' "
        f"+password '{vc_password}' +show-unreleased "
        "com vmware vcenter namespacemanagement clusters get "
        "--cluster domain-c11 +formatter json | jq -r '.api_servers | .[]'"
    )
    return execute_remote_command(vc_ip, username, root_password, vc_password, dcli_command)


def main(url):
    filename = re.sub(r'[:/]', '_', url.split('//')[1])  # Remove the 'http://' or 'https://' part
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testbeds", filename)
    data = download_json(url, filename)
    if not data:
        return

    vc_ip = data.get('vc', {}).get('1', {}).get('ip', '')
    vc_password = data.get('vc', {}).get('1', {}).get('password', '')
    root_password = data.get('vc', {}).get('1', {}).get('root_password', '')
    username = "root"

    print(f"VC IP: {vc_ip}")
    print("Retrieving master node details...")
    decrypt_command = "/usr/lib/vmware-wcp/decryptK8Pwd.py"
    output = execute_remote_command(vc_ip, username, root_password, vc_password, decrypt_command)

    if output:
        lines = output.strip().split("\n")
        if len(lines) >= 7:
            master_ip = lines[5].strip().split(":")[1].strip()
            master_password = lines[6].strip().replace("PWD: ", "")

            print(f"Extracted VC IP: {vc_ip}, VC Password: {vc_password}")
            print(f"Master IP: {master_ip}, Master Password: {master_password}")

            # Retrieve API servers
            api_servers_output = get_api_servers(vc_ip, username, root_password, vc_password)
            filtered_nodes = [line for line in api_servers_output.split("\n") if
                              line.startswith("10") and line.strip() != master_ip]

            # Create sp_nodes structure
            sp_nodes = {
                "nodes": filtered_nodes,
                "password": master_password,
                "vc_user": "administrator@vsphere.local",
                "vc_ip": vc_ip,
                "vc_password": vc_password,
                "vc_root_password": root_password
            }

            # Print sp_nodes.json
            print(json.dumps(sp_nodes, indent=4))
        else:
            print("ERROR: Output did not contain enough information.")
    else:
        print("ERROR: Could not retrieve master node details.")


if __name__ == "__main__":
    url = input("Enter json url: ")
    main(url)