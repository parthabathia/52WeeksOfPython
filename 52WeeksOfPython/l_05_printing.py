import nmap
from l_03_functions import create_devices
from pprint import pprint
from operator import itemgetter
from tabulate import tabulate
from datetime import datetime
from time import sleep
from random import choice

devices = create_devices(5)

print("\n\nUsing Print")
print(devices)

print("\n\nUsing Pprint")
pprint(devices)

print("\n\nUsing Loop")
for device in devices:
    sleep(0.1)
    device["last_heard"] = str(datetime.now())
    print(device)

print("\n\nUsing Tabulate")
print(
    tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys")
)

print("\n\nUsing Loop and F-string")
print("   Name      Vendor : OS       IP Address         Last Heard")
print("   ----      ------   -----    ------------       ----------")
for device in devices:
    print(
        f'{device["name"]:>7}  {device["vendor"]:>10} : {device["os"]:<6}   {device["ip"]:<15}    {device["last_heard"][:-4]}'
    )

print("\n\nSame thing, but sorted descending using last_heard")
for device in sorted(devices, key=itemgetter("last_heard"), reverse=True):
    print(
        f'{device["name"]:>7}  {device["vendor"]:>10} : {device["os"]:<6}  {device["ip"]:<15}  {device["last_heard"][:-4]}'
    )

print("\n\nMultiple Print Statements, Same Line")
print("Testing Devices:")
for device in devices:
    print(f"--- testing device {device['name']} ... ", end="")
    sleep(choice([0.1, 0.2, 0.3, 0.4]))
    print("done.")
print("Testing Complete")

nm = nmap.PortScanner()
while True:

    ip = input("\nInput IP Address to scan: ")
    if not ip:
        break

    print(f"\n--- beginning scan of {ip}")
    output = nm.scan(ip, '22-1024')
    print(f"--- --- command: {nm.command_line()}")

    print("----- nmap scan output -------------------")
    pprint(output)
