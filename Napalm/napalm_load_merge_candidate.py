from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'}  # Enter enable password of the device
# Enter IP address of the device
ios = driver('10.1.1.10', 'alex', 'cisco', optional_args=optional_args)
ios.open()

ios.load_merge_candidate(filename="acl.txt")

diff = ios.compare_config()

if len(diff) > 0:
    print(diff)
    answer = input("Commit changes? [yes/no]")
    if answer == "yes":
        print("Committing Config")
        ios.commit_config()
        print("Config Committed")
    else:
        print("Discarding Config")
        ios.discard_config()
else:
    print("No Changes Required")
    ios.discard_config()

answer = input("Would you like to rollback? [yes/no]")
if answer == "yes":
    print("Rolling back")
    ios.rollback()
    print("Rollback Complete")

ios.close()
