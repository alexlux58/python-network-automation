from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'}  # Enter enable password of the device
# Enter IP address of the device
ios = driver('10.1.1.10', 'alex', 'cisco', optional_args=optional_args)
ios.open()

ios.load_replace_candidate(filename="router_config.txt")

diff = ios.compare_config()


if len(diff) > 0:
    print(diff)
    print("Committing Config")
    ios.commit_config()
    print("Config Committed")
else:
    print("No Changes Required")
    ios.discard_config()

ios.close()
