# Justin Edwards
# Classroom Network Lab

# Classroom 1 - 30 computers and printers
# Classroom 2 - 30 computers and printers
# Classroom 3 - 14 computers
# Classroom 4 - 14 computers
# Classroom 5 - 14 computers
# Lab 1 - 6 computers
# Lab 2 - 6 computers
# Total - 114 addresses

# 138.191.0.0/25 = 64 addresses
# 138.191.0.0/27 = 128 addresses

import ipaddress
import time # I honestly have no clue why this was added in the lecture video

ip = '138.191.0.0/25'

ipInterface = ipaddress.ip_interface(ip)
ipNetwork = ipInterface.network

# divide into 4 subnets
subnetted = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff=2))

# classroom 1 & 2 need 30 each, use one 32 address subnet for each
classroom1 = subnetted[0]
classroom2 = subnetted[1]

# classroom 3 and 4 add up to 28, divide subnet into two
subnetted2 = list(ipaddress.ip_network(subnetted[2]).subnets())

# Each class needs 14, use one 16 address subnet for each
classroom3 = subnetted2[0]
classroom4 = subnetted2[1]

# classroom 5 & lab 1 and 2 add up to 26 total, divide 32 address subnet
subnetted3 = list(ipaddress.ip_network(subnetted[3]).subnets())

# classroom 5 needs 14, use one 16 address subnet
classroom5 = subnetted3[0]

# lab 1 and 2 only need 6 each, divide 16 address subnet
subnetted4 = list(ipaddress.ip_network(subnetted3[1]).subnets())

# lab 1 and 2 need 6 addresses each, use one 8 address subnet for each
lab1 = subnetted4[0]
lab2 = subnetted4[1]


def printOut(name, subnet, devices):
    print(name)
    print('----------------------------------------------------------------')
    print("The network address with the subnet mask is: {}".format(subnet))
    print("The network address is: {}".format(subnet.network_address))
    print("The broadcast address is: {}".format(subnet.broadcast_address))
    print("The number of computers is: {}".format(devices))
    print("The valid host range is: {0} - {1}".format(subnet.network_address + 1, subnet.broadcast_address - 1))
    print()

printOut("Classroom 1", classroom1, 30)
printOut("Classroom 2", classroom2, 30)
printOut("Classroom 3", classroom3, 14)
printOut("Classroom 4", classroom4, 14)
printOut("Classroom 5", classroom5, 14)
printOut("Lab 1", lab1, 6)
printOut("Lab 2", lab2, 6)
