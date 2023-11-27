# Python NAPALM (Network Automation and Programmability Abstraction Layer with Multivendor support) is a Python library that provides
# a unified interface to automate and interact with different network devices and Operating Systems.
# It's particularly relevant to your interests in programming, DevOps, and cyber security, as it streamlines network automation tasks.

from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'}  # Enter enable password of the device
# Enter IP address of the device
ios = driver('10.1.1.10', 'alex', 'cisco', optional_args=optional_args)
ios.open()

print(dir(ios))

output = ios.get_arp_table()
for item in output:
    print(item)

dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

with open('arp.txt', 'w') as f:
    f.write(dump)

ios.close()
