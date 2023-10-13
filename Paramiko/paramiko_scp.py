import paramiko
from scp import SCPClient

port = 22
username = "u1"
password = "cisco"
ip_address = "127.0.0.1"

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, port=port, username=username,
                   password=password, allow_agent=False, look_for_keys=False)

scp = SCPClient(ssh_client.get_transport())

# Copy the file from the local host to the remote host
scp.put('test.txt', recursive=True, remote_path='/home/u1/')

# Copy the file from the remote host to the local host
scp.get('/home/u1/test.txt', 'test2.txt')

scp.close()
ssh_client.close()
