import pickle
import json

friends = {"Dan": [20, "London", 8052795912],
           "maria": [25, "Madrid", 4444444444]}

with open("friends.dat", "wb") as f:
    pickle.dump(friends, f)

with open("friends.dat", "rb") as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)


with open('friends.json', 'w') as f:
    json.dump(friends, f, indent=4)

json_string = json.dumps(friends, indent=4)
print(json_string)


with open('friends.json', 'rt') as f:
    obj = json.load(f)
    print(type(obj))
    print(obj)
