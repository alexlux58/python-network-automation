import paramiko

# SSH Client and Server Capabilities: Paramiko can be used to create SSH clients for connection and interaction with SSH servers, as well as to implement SSH servers.

# SFTP Client and Server: Supports SFTP (SSH File Transfer Protocol) for secure file transfer over SSH.

# Key Management: It includes support for managing SSH keys and authentication methods, which is crucial for secure connections.

# Channel Management: Paramiko allows you to create and manage channels over an SSH connection, which is essential for executing commands remotely and transferring data.

# Encryption and Security: Implements robust encryption algorithms and security mechanisms, making it suitable for secure network operations and automation tasks.

# creating an ssh client object
ssh_client = paramiko.SSHClient()
# print(type(ssh_client))

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('Connecting to 10.1.1.10')
ssh_client.connect(hostname='10.1.1.10', port='22', username='u1', password='cisco',
                   look_for_keys=False, allow_agent=False)


# checking if the connection is active
print(ssh_client.get_transport().is_active())

# sending commands
# ...

print('Closing connection')
ssh_client.close()
