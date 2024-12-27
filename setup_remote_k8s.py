import os
import subprocess
import time
import paramiko
import warnings


def connect_ssh(remote_ip, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Connecting to remote host...")
    ssh.connect(
        remote_ip,
        username='root',
        password=password,
        timeout=30,
        allow_agent=False,
        look_for_keys=False
    )
    return ssh


def setup_socks_proxy(remote_ip, password):
    print("Setting up SOCKS proxy...")
    proxy_cmd = (
        f'sshpass -p "{password}" /usr/bin/ssh -n '
        f'-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null '
        f'-D 1080 -N root@{remote_ip}'
    )
    proxy_process = subprocess.Popen(proxy_cmd, shell=True, stdin=subprocess.PIPE)
    time.sleep(3)
    os.environ['https_proxy'] = 'socks5://localhost:1080'
    return proxy_process


def retrieve_kubectl_config(ssh):
    print("Retrieving kubectl config...")
    stdin, stdout, stderr = ssh.exec_command('cat /etc/kubernetes/admin.conf')
    config_content = stdout.read().decode().strip()

    if not config_content:
        stdin, stdout, stderr = ssh.exec_command('cat $HOME/.kube/config')
        config_content = stdout.read().decode().strip()

    if not config_content:
        raise Exception("Could not retrieve kubectl config from remote host")

    return config_content


def save_kubectl_config(remote_ip, config_content):
    config_path = os.path.expanduser(f'~/.kube/config_{remote_ip}')
    os.makedirs(os.path.dirname(config_path), exist_ok=True)

    config_lines = config_content.splitlines()
    for i, line in enumerate(config_lines):
        if 'server:' in line:
            config_lines[i] = f'    server: https://{remote_ip}:6443'
            config_lines.insert(i + 1, '    proxy-url: socks5://localhost:1080')
            break

    with open(config_path, 'w') as f:
        f.write('\n'.join(config_lines))

    print(f"Config saved to {config_path}")
    os.environ['KUBECONFIG'] = config_path
    return config_path


def enable_allow_tcp_forwarding(ssh):
    print("AllowTcpForwarding is disabled. Attempting to enable it...")
    # Add or modify AllowTcpForwarding in sshd_config
    ssh.exec_command('echo "AllowTcpForwarding yes" >> /etc/ssh/sshd_config')

    # Restart the SSH service
    ssh.exec_command('systemctl restart sshd')
    print("AllowTcpForwarding has been enabled and SSH service restarted.")


def check_and_enable_tcp_forwarding(ssh):
    print("Checking if AllowTcpForwarding is enabled...")
    stdin, stdout, stderr = ssh.exec_command('grep -i "AllowTcpForwarding" /etc/ssh/sshd_config')
    result = stdout.read().decode().strip()

    if "AllowTcpForwarding no" in result:
        enable_allow_tcp_forwarding(ssh)
    elif not result or "AllowTcpForwarding yes" not in result:
        enable_allow_tcp_forwarding(ssh)
    else:
        print("AllowTcpForwarding is already enabled.")


def test_kubectl_connection():
    print("Testing kubectl connection...")
    result = subprocess.run(['kubectl', 'get', 'nodes'], capture_output=True, text=True)
    if result.returncode == 0:
        print("Connection successful!")
        print(result.stdout)
    else:
        print("Connection test failed:")
        print(result.stderr)


def cleanup(proxy_process, ssh, remote_ip):
    subprocess.run(['pkill', '-f', f'/usr/bin/ssh -D 1080 -N root@{remote_ip}'])
    if ssh:
        ssh.close()


def setup_k8s_remote_access(remote_ip, password):
    ssh = None
    proxy_process = None

    try:
        ssh = connect_ssh(remote_ip, password)
        check_and_enable_tcp_forwarding(ssh)
        proxy_process = setup_socks_proxy(remote_ip, password)
        config_content = retrieve_kubectl_config(ssh)
        config_path = save_kubectl_config(remote_ip, config_content)
        test_kubectl_connection()

        print("*"*100)
        print(f"sshpass -p '{password}' /usr/bin/ssh -D 1080 -N root@{remote_ip}")
        print(f"export KUBECONFIG={config_path}")

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        cleanup(proxy_process, ssh, remote_ip)


if __name__ == "__main__":
    remote_ip = input("Enter remote K8s node IP: ")
    password = input("Enter password: ")
    setup_k8s_remote_access(remote_ip, password)