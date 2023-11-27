from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'}  # Enter enable password of the device
# Enter IP address of the device
ios = driver('10.1.1.10', 'alex', 'cisco', optional_args=optional_args)
ios.open()

output = ios.get_facts()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_arp_table()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_interfaces()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_interfaces_counters()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_interfaces_ip()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_lldp_neighbors()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_lldp_neighbors_detail()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_mac_address_table()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_ntp_peers()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_ntp_servers()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_ntp_stats()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_optics()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_probes_config()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_probes_results()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_route_to()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_snmp_information()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_users()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.ping('10.1.1.20', count=2, source="1.1.1.1")
ping = json.dumps(output, sort_keys=True, indent=4)
print(ping)


ios.close()
