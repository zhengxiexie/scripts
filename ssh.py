import os
import json
import subprocess
import sys
import pexpect

def download_json(url, filename="testbedInfo.json"):
    # Use wget to download the file
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    else:
        subprocess.run(["wget", "-O", filename, url], check=True)
        with open(filename, "r") as file:
            return json.load(file)

def execute_remote_command(ip, username, password, command):
    print("-"*20)
    print(f"VC IP: {ip}")
    print(f"VC PWD: {password}")
    print(f"VC COMMAND: /usr/lib/vmware-wcp/decryptK8Pwd.py")
    ssh_command = f"sshpass -p '{password}' ssh -o StrictHostKeyChecking=no {username}@{ip} {command}"
    result = subprocess.run(ssh_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

def open_interactive_ssh_session(ip, username, password):
    command = f"sshpass -p '{password}' ssh -o StrictHostKeyChecking=no  {username}@{ip}"
     # Use pbcopy to copy the string to the clipboard
    process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    process.communicate(input=command.encode('utf-8'))


def main(url):
    # Download and parse JSON data using wget
    data = download_json(url)

    # Extract the necessary details from the JSON data
    vc = data['vc']['1']
    ip = vc['ip']
    root_password = vc['root_password']
    username = "root"  # Assuming root username based on the password provided

    # Execute the decryptK8Pwd.py script on the first node
    command = "/usr/lib/vmware-wcp/decryptK8Pwd.py"
    stdout, stderr = execute_remote_command(ip, username, root_password, command)

    # Parse the output to extract the IP and password
    lines = stdout.splitlines()
    new_ip = None
    new_password = None
    for line in lines:
        if "IP:" in line:
            new_ip = line.split(":")[1].strip()
        elif "PWD:" in line:
            new_password = line.split(":")[1].strip()

    if new_ip and new_password:
        print("-"*20)
        print(f"MASTER NODE IP: {new_ip}")
        print(f"MASTER NODE PWD: {new_password}")
        # Open an interactive SSH session to the new node
        open_interactive_ssh_session(new_ip, username, new_password)
    else:
        print("Failed to extract IP and password from the output")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    main(url)
