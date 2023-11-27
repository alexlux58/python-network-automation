# from netmiko import Netmiko
# connection = Netmiko(host='10.1.1.10', port='22', username='u1', password='cisco', device_type='cisco_ios')

# Netmiko is a Python library that simplifies the process of managing network devices via SSH.
# It is particularly relevant to your interests in Python programming, DevOps, and network automation.
# Developed by Kirk Byers, Netmiko is part of a larger group of open-source projects focused on network automation,
# including the well-known NAPALM (Network Automation and Programmability Abstraction Layer with Multivendor support).

from netmiko import ConnectHandler
# creating a dictionary for the device to connect to
cisco_device = {
    # device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
    'device_type': 'cisco_ios',
    'host': '10.1.1.10',
    'username': 'u1',
    'password': 'cisco',
    'port': 22,             # optional, default 22
    'secret': 'cisco',      # this is the enable password
    'verbose': True         # optional, default False
}

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)

# sending a command and getting the output
output = connection.send_command('sh ip int brief')
print(output)

# closing the connection
print('Closing connection')
connection.disconnect()
