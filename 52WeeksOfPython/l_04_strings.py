from pprint import pprint

device1_str = "  r3-L-n7, cisco, catalyst 2960, ios  "

# split
print("String Strip, Split, Replace")
device1 = device1_str.split(",")
print("device1 using split:")
print("    ", device1)

# strip
device1 = device1_str.strip().split(",")
print("device1 using strip and split:")
print("    ", device1)

# remove blanks
device1 = device1_str.replace(" ", "").split(",")
print("device1 replaced blanks using split:\n    ", device1)

# remove blanks and change comma to colon
device1_str_colon = device1_str.replace(" ", "").replace(",", ":")
print("device1 replaced blanks, comma to colon:")
print("    ", device1_str_colon)

# loop with strip and split
device1 = []
for item in device1_str.split(","):
    device1.append(item.strip())
print("device1 using loop and strip for each item")
print("    ", device1)

# strip and split, single line using list comprehension
device1 = [item.strip() for item in device1_str.split(",")]
print("device1 using list comprehension")
print("    ", device1)

# ignoring case
print("\n\nIgnoring Case")
model = "CSR1000V"
if model == "csr1000v":
    print(f"matched : {model}")
else:
    print(f"didn't match : {model}")

model = "CSR1000V"
if model.lower() == "csr1000v":
    print(f"matched using lower() : {model}")
else:
    print(f"didn't match : {model}")

# finding sub-string
print("\n\nFinding Substring")
version = "Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.11.1a, RELEASE SOFTWARE (fc1)"
expected_version = "Version 16.11.1a"
index = version.find(expected_version)
if index >= 0:
    print(f"found version: {expected_version} at location {index} ")
else:
    print(f"not found: {expected_version}")

# separating version string components
print("\n\nSeparating version string component")
version_info = version.split(",")
for item in version_info:
    print(f"Version part: {item.strip()}")

show_interface_stats = """
GigabitEthernet1
          Switching path    Pkts In     Chars In    Pkts Out    Chars Out
               Processor      25376      1529598        8242       494554
             Route Cache          0            0           0            0
       Distributed Cache     496298     60647894      673003    218461079
                   Total     521674     62177492      681245    218955633
GigabitEthernet2
          Switching path    Pkts In     Chars In    Pkts Out    Chars Out
               Processor         19         1140           0            0
             Route Cache          0            0           0            0
       Distributed Cache       6077       663304           0            0
                   Total       6896       664444           0            0
Interface GigabitEthernet3 is disabled

Loopback21
          Switching path    Pkts In     Chars In    Pkts Out    Chars Out
               Processor          0            0           0            0
             Route Cache          0            0           0            0
       Distributed Cache          0            0           0            0
                   Total          0            0           0            0
Loopback55
          Switching path    Pkts In     Chars In    Pkts Out    Chars Out
               Processor          0            0           3          241
             Route Cache          0            0           0            0
       Distributed Cache          0            0           0            0
                   Total          0            0           3          241
Loopback100
          Switching path    Pkts In     Chars In    Pkts Out    Chars Out
               Processor          0            0          43         2806
             Route Cache          0            0           0            0
       Distributed Cache          0            0           0            0
                   Total          0            0          43         2806
"""

interface_counters = dict()
show_interface_stats_lines = show_interface_stats.splitlines()
for index, stats_lines in enumerate(show_interface_stats_lines):
    if stats_lines.find('GigabitEthernet', 0) == 0:
        totals_lines = show_interface_stats_lines[index + 5]
        interface_counters[stats_lines] = totals_lines.split()[1:]

print("\n\n----- Interface Counters -------------------")
pprint(interface_counters)

show_arp = """
Protocol    Address         Age (min)   Hardware Addr    Type   Interface
Internet    10.10.20.48             -   0050.56bb.e99c   ARPA   GigabitEthernet
Internet    10.10.20.200           14   0050.56bb.8be2   ARPA   GigabitEthernet
Internet    10.10.20.254            0   0896.ad9e.844c   ARPA   GigabitEthernet
"""

arp_table = dict()
for arp_line in show_arp.splitlines():
    if arp_line.find('Internet', 0) == 0:
        arp_table[arp_line.split()[1]] = arp_line.split()[3]

print("\n\n----- ARP Table --------------------")
pprint(arp_table)
