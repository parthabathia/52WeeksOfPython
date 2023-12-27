from pprint import pprint
import copy
from random import choice
from util.create_utils import create_network

device = {
    "name": "r3-L-n7",
    "vendor": "cisco",
    "model": "catalyst 2960",
    "os": "ios",
    "interfaces": []
}

print("\n\n----- device with no interfaces -------------------")
for key, value in device.items():
    print(f"{key:>16s} : {value}")

interfaces = list()
for index in range(0, 8):
    interface = {
        "name": "g/0/0/" + str(index),
        "speed": choice(["10", "100", "1000"])
    }
    interfaces.append(interface)

device["interfaces"] = interfaces

print("\n\n----- device with interfaces --------------------")
for key, value in device.items():
    if key != "interfaces":
        print(f"{key:>16s} : {value}")
    else:
        print(f"{key:>16s} : ")
        for interface in interfaces:
            print(f"\t\t\t\t\t{interface}")

print()
print("\n----- device with interfaces using pprint ----------------------")
pprint(device)

print("\n----- network with devices and interfaces ----------------------")
network = create_network(num_devices=4, num_subnets=4)
pprint(network)

print("\n----- information about the network ------------------------")
print(f"-- number of subnets: {len(network['subnets'])}")
print(f"-- list of subnets: {network['subnets'].keys()}")
print(f"-- list of subnets w/o extraneous: {', '.join(network['subnets'])}")

print("\n----- network and devices nicely formatted ---------------------")
for subnet_address, subnet in network["subnets"].items():
    print(f"\n-- subnet: {subnet_address}")
    for device in subnet["devices"]:
        print(f"   |--device: {device['name']:8} {device['ip']:10} {device['vendor']:>8} : {device['os']:<5}")

print("\n----- python assignment vs copy vs deepcopy ----------------------")
print("\n-- assignment")
network_assign = network
network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "different name assigned"
print(f"  --- network == network_assign : {network == network_assign}")

print("\n-- shallow copy")
network_copy = copy.copy(network)
network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "different name assigned using copy"
print(f"  --- network == network_copy   : {network == network_copy}")

print("\n-- assignment")
network_deepcopy = copy.deepcopy(network)
network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "different name assigned using deepcopy"
print(f"  --- network == network_deepcopy : {network == network_deepcopy}")
