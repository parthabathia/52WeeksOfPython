# from flask import Flask
from tabulate import tabulate
from util.create_utils import create_devices

if __name__ == '__main__':
    devices = create_devices(num_devices=5, num_subnets=4)
    print('\n', tabulate(devices, headers='keys'))

list1 = ['x', 'y', 'z', 'a1']
