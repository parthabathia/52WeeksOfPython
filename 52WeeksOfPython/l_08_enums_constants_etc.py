from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from enum import Enum

# CONSTANTS: just use the name itself, e.g. CISCO
CISCO = "cisco"
JUNIPER = "juniper"
ARISTA = "arista"


# CLASS: use class name and class variable, e.g. Vendor.CISCO
class Vendor:
    CISCO = "cisco"
    JUNIPER = "juniper"
    ARISTA = "arista"


# ENUM: use class name and enum, which has 'name' and 'value' attributes
#   e.g. Vendor.CISCO.name or Vendor.CISCO.value
class Vendor(Enum):
    CISCO = 1
    JUNIPER = 2
    ARISTA = 3


# ENUM: use class name and enum, which has 'name' and 'value' attributes
#   e.g. Vendor.CISCO.name or Vendor.CISCO.value
class Vendor(Enum):
    CISCO = "cisco"
    JUNIPER = "juniper"
    ARISTA = "arista"


devices = []

for device_index in range(20):
    device = dict()
    device["name"] = (
            choice(['r2', 'r3', 'r4', 'r6', 'r10'])
            + choice(['L', 'U'])
            + choice(string.ascii_letters)
    )

    # USING LITERALS: RANDOM VENDOR FROM CHOICE OF CISCO, JUNIPER, ARISTA
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
    device['ip'] = '10.0.0' + str(device_index)

    # USING CONSTANTS: RANDOM VENDOR FROM CHOICE OF CISCO, JUNIPER, ARISTA
    device['vendor'] = choice([CISCO, JUNIPER, ARISTA])
    if device['vendor'] == CISCO:
        device['os'] = choice(['ios', 'iosxe', 'iosxr', 'nexus'])
        device['version'] = choice(['12.1(T).04', '14.07x', '8.12(S).010', '20.5P'])
    elif device['vendor'] == JUNIPER:
        device['os'] = 'junos'
        device['version'] = choice(['J6.23.1', '8.43.I2', '6.4S', '6.03P'])
    elif device['vendor'] == ARISTA:
        device['os'] = 'eos'
        device['version'] = choice(['2.45', '2.55', '2.9.145', '3.01'])
    device['ip'] = '10.0.0' + str(device_index)

    # USING CLASS: RANDOM VENDOR FROM CHOICE OF CISCO, JUNIPER, ARISTA
    device['vendor'] = choice([Vendor.CISCO, Vendor.JUNIPER, Vendor.ARISTA])
    if device['vendor'] == Vendor.CISCO:
        device['os'] = choice(['ios', 'iosxe', 'iosxr', 'nexus'])
        device['version'] = choice(['12.1(T).04', '14.07x', '8.12(S).010', '20.5P'])
    elif device['vendor'] == Vendor.JUNIPER:
        device['os'] = 'junos'
        device['version'] = choice(['J6.23.1', '8.43.I2', '6.4S', '6.03P'])
    elif device['vendor'] == Vendor.ARISTA:
        device['os'] = 'eos'
        device['version'] = choice(['2.45', '2.55', '2.9.145', '3.01'])
    device['ip'] = '10.0.0' + str(device_index)

    # USING ENUMS (NAME): RANDOM VENDOR FROM CHOICE OF CISCO, JUNIPER, ARISTA
    device['vendor'] = choice([Vendor.CISCO.name, Vendor.JUNIPER.name, Vendor.ARISTA.name])
    if device['vendor'] == Vendor.CISCO.name:
        device['os'] = choice(['ios', 'iosxe', 'iosxr', 'nexus'])
        device['version'] = choice(['12.1(T).04', '14.07x', '8.12(S).010', '20.5P'])
    elif device['vendor'] == Vendor.JUNIPER.name:
        device['os'] = 'junos'
        device['version'] = choice(['J6.23.1', '8.43.I2', '6.4S', '6.03P'])
    elif device['vendor'] == Vendor.ARISTA.name:
        device['os'] = 'eos'
        device['version'] = choice(['2.45', '2.55', '2.9.145', '3.01'])
    device['ip'] = '10.0.0' + str(device_index)

    # USING ENUMS (VALUE): RANDOM VENDOR FROM CHOICE OF CISCO, JUNIPER, ARISTA
    device['vendor'] = choice([Vendor.CISCO.value, Vendor.JUNIPER.value, Vendor.ARISTA.value])
    if device['vendor'] == Vendor.CISCO.value:
        device['os'] = choice(['ios', 'iosxe', 'iosxr', 'nexus'])
        device['version'] = choice(['12.1(T).04', '14.07x', '8.12(S).010', '20.5P'])
    elif device['vendor'] == Vendor.JUNIPER.value:
        device['os'] = 'junos'
        device['version'] = choice(['J6.23.1', '8.43.I2', '6.4S', '6.03P'])
    elif device['vendor'] == Vendor.ARISTA.value:
        device['os'] = 'eos'
        device['version'] = choice(['2.45', '2.55', '2.9.145', '3.01'])
    device['ip'] = '10.0.0' + str(device_index)

    devices.append(device)

print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version", )), headers="keys"))
