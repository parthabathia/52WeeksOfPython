from random import choice
import string
from tabulate import tabulate
from pprint import pprint
from operator import itemgetter

devices = list() # empty list for holding devices

# for loop for creating large number of devices
for index in range(10):

    # create device dictionary
    device = dict()

    # random device name
    device["name"] = (
        choice(['r2', 'r3', 'r4', 'r6', 'r10'])
        + choice(['L', 'U'])
        + choice(string.ascii_letters)
    )

    # random vendor from choice of cisco, juniperr, arista
    device['vendor'] = choice(['cisco', 'juniper', 'arista'])
    if device['vendor'] == 'cisco':
        device['os'] = choice(['ios', 'iosxe', 'iosxr', 'nexus'])
        device['version'] = choice(['12.1(T).04', '14.07x', '8.12(S).010', '20.5P'])
    elif device['vendor'] == 'juniper':
        device['os'] = 'junos'
        device['version'] = choice(['J6.23.1', '8.43.I2', '6.4S', '6.03P'])
    elif device['vendor'] == 'arista':
        device['os'] = 'eos'
        device['version'] = choice(['2.45', '2.55', '2.9.145', '3.01'])
    device['ip'] = '10.0.0.' + str(index)

    print()
    for key, value in device.items():
        print(f'{key:>16s} : {value}')

    devices.append(device)

# use print to print data as-is
print("\n--------- Devices as List of Dicts -------------")
pprint(devices)

# using tabulate to print table of devices
print("\n----- Sorted Devices in Tabular Format -------")
sorted_devices = sorted(devices, key=itemgetter('vendor', 'os', 'version'))
print(tabulate(sorted_devices, headers='keys'))