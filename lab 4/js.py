import json

with open('sample-data.json') as f:
    data = json.load(f)

print("""Interface Status
================================================================================""")

print("DN                                                 Description           Speed    MTU  ")

print("-------------------------------------------------- --------------------  ------  ------")

for i in range(3):
    print(data["imdata"][i]["l1PhysIf"]["attributes"]["dn"],end="")
    print("                              ",end="")
    print(data["imdata"][i]["l1PhysIf"]["attributes"]["speed"],end="   ")
    print(data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])