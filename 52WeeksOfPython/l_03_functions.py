from random import choice
import string
from tabulate import tabulate


def create_devices(num_devices=1, num_subnets=1):

    # create list of devices
    created_devices = []

    if num_devices > 254 or num_subnets > 254:
        print('\nError: Too many devices or subnets requested.')
        return created_devices

    for subnet_index in range(1, num_subnets+1):

        for device_index in range(1, num_devices+1):

            # create device dictionary
            device = dict()

            # provide data to devices
            device["name"] = (
                    choice(['r2', 'r3', 'r4', 'r6', 'r10'])
                    + choice(['L', 'U'])
                    + choice(string.ascii_letters)
            )

            # random vendor from choice of cisco, juniper, arista
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
            device['ip'] = '10.0.' + str(subnet_index) + '.' + str(device_index)

            created_devices.append(device)

    return created_devices


if __name__ == '__main__':

    devices = create_devices(num_devices=5, num_subnets=4)
    print('\n', tabulate(devices, headers='keys'))
