from util.create_utils import create_devices
from pprint import pprint
from random import randint, uniform
from datetime import datetime

devices = create_devices(num_subnets=2, num_devices=25)
print("   Name      Vendor : OS       IP Address         Version")
print("   ----      ------   -----    ------------       ----------")
for device in devices:
    print(
        f'{device["name"]:>7}  {device["vendor"]:>10} : {device["os"]:<6}   {device["ip"]:<15}    {device["version"]}'
    )

print("\n\n   Name      Vendor : OS       IP Address         Version")
print("   ----      ------   -----    ------------       ----------")
for device in devices:
    if device["vendor"].lower() == "cisco":
        print(
            f'{device["name"]:>7}  {device["vendor"]:>10} : {device["os"]:<6}   {device["ip"]:<15}    {device["version"]}'
        )
print("\n\n----- Starting comparison of device names ----------------------")
for index, device_a in enumerate(devices):
    for device_b in devices[index + 1:]:
        if device_a["name"] == device_b["name"]:
            print(f'Found Match! {device_a["name"]} for both {device_a["ip"]} and {device_b["ip"]}')

print("----- Comparison of device names completed")

print("\n----- Create table of arbitrary 'standard' version for each vendor:os --------")
standard_versions = dict()
for device in devices:
    vendor_os = device["vendor"] + ":" + device["os"]
    if vendor_os not in standard_versions:
        standard_versions[vendor_os] = device["version"]
pprint(standard_versions)

print("\n----- Create table of non-compliant version for each vendor:os --------")
non_compliant_devices = dict()
for vendor_os, _ in standard_versions.items():
    non_compliant_devices[vendor_os] = []

for device in devices:
    vendor_os = device["vendor"] + ":" + device["os"]
    if device["version"] != standard_versions[vendor_os]:
        non_compliant_devices[vendor_os].append(device["ip"] + " version:" + device["version"])

pprint(non_compliant_devices)

print("\n\n----- Assignment, copy and deep copy  --------------------")
devices2 = devices
devices[0]["name"] = "this is a dumb device name"
if devices2 == devices:
    print("\n    Assignment and modification: device2 still equals devices")
    print("    ----> Moral: Assignment is not the same as copy!")
else:
    print("    Huh?")

from copy import copy
from copy import deepcopy

devices2 = copy(devices)
devices2[0]["name"] = "this is also a dumb device name"
if devices2 == devices:
    print("\n    Shallow copy and modification: device2 still equals devices")
    print("    ----> Moral: 'copy()' only does a shallow (1st level) copy!")
    print("    ----> Result: Uh-oh - I just screwed up the original version!!")
else:
    print("    Huh?")

devices2 = deepcopy(devices)
devices2[0]["name"] = "this is another dumb device name"
if devices2 == devices:
    print("    Huh?")
else:
    print("\n    Deep copy and modification: device2 no longer equals devices")
    print("    ----> Moral: 'deepcopy()' gives you a complete copy of the original!")
    print("    ----> Result: I can do whatever I want with my copy, without touching the original!!")

new_set_of_devices = create_devices(num_subnets=2, num_devices=25)
if new_set_of_devices == devices:
    print("    Huh?")
else:
    print("\n    Comparisons of complex, deep data is easy in Python")
    print("    ----> Moral: you can compare any two data structures, no matter how deep")

print("\n\n----- Comparisons for implementing SLAs ----------------\n")
SLA_AVAILABILITY = 96
SLA_RESPONSE_TIME = 1.0

devices = create_devices(num_subnets=2, num_devices=25)
for device in devices:
    device["availability"] = randint(94, 100)
    device["response_time"] = uniform(0.5, 1.1)

    if device['availability'] < SLA_AVAILABILITY:
        print(f"{datetime.now()}: {device['name']:6} - Availability {device['availability']} < {SLA_AVAILABILITY}")
    if device['response_time'] > SLA_RESPONSE_TIME:
        print(f"{datetime.now()}: {device['name']:6} - Response Time {device['response_time']} < {SLA_RESPONSE_TIME}")
