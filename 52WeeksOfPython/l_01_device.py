import sys
from pprint import pprint

device = {
    'name': 'sbx-n9kv-a',
    'vendor': 'cisco',
    'model': 'Nexus9000 C9300v Chasis',
    'os': 'nxos',
    'version': '9.3(3)',
    'ip': '10.1.1.1',
}

# simple print
print("\n______ SIMPLE PRINT _________________")
print("device:", device)
print("device name:", device['name'])

# pretty print
print("\n______ PRETTY PRINT _________________")
pprint(device)

# for loop, nicely formatted print
print("\n______ FOR LOOP, USING F-STRING _________________")
for key, value in device.items():
    print(f'{key:>10s} : {value}')