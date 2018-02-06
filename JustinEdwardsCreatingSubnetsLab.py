import ipaddress


def bitMask(bits):
    mask = ''
    for x in range(0, bits):
        mask += '1'
    for x in range(0, 32 - bits):
        mask += '0'
    decimal = str(int(mask[0:8], 2)) + '.' + str(int(mask[8:16], 2)) + '.' + str(int(mask[16:24], 2)) + '.' + str(int(mask[24:32], 2))
    mask = mask[0:8] + '.' + mask[8:16] + '.' + mask[16:24] + '.' + mask[24:32]

    print('\nFor a {} bit mask:'.format(str(bits)))
    print('\tThe binary version is: {}'.format(mask))
    print('\tThe decimal version is: {}'.format(decimal))


def maskInfo(ip):
    ipInterface = ipaddress.ip_interface(ip)
    ipNetwork = ipInterface.network

    print('\nFor the IP address {}:'.format(ip))
    print('\tNetwork address: {}'.format(ipNetwork.network_address))
    print('\tBroadcast address: {}'.format(ipNetwork.broadcast_address))
    print('\tNumber of host addresses: {}'.format(len(list((ipNetwork).hosts()))))
    print('\tValid host address range {0} - {1}'.format((ipNetwork.network_address + 1), (ipNetwork.broadcast_address - 1)))


def bitsnHosts(ip):
    ipInterface = ipaddress.ip_interface(ip)
    ipNetwork = ipInterface.network
    print('\nWith the subnet mask {} answer the following: '.format(ip))
    print('\tNumber of bits used in subnet mask: {}'.format(ipNetwork.prefixlen))
    print('\tNumber of hosts: {}'.format(len(list(ipNetwork.hosts()))))


def subnet(ip):
    print('\nYou are a manager of a network that has 56 remote site and you have one Class B license. '
          'What subnet mask would you use with having the max amount of hosts at each site 1000?')
    # Class B license has a /16 mask with 65,534 hosts, enough to cover 1000 hosts per site at 56,000
    ipInterface = ipaddress.ip_interface(ip)
    ipNetwork = ipInterface.network
    bitsBorrowed = 6    # Need to borrow 6 bits to have 2^6 = 64 bits to have enough for the 54 sites.
    ipSubnetLength = ipNetwork.prefixlen + bitsBorrowed
    print('\tThe subnet mask length is {}'.format(ipSubnetLength))
    print('\tThe 56 subnets needed are less than the {} subnets created.'.format(len(list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff=bitsBorrowed)))))
    ipSubnet = str('10.10.10.10/' + str(ipSubnetLength))
    ipSubnetAddress = ipaddress.ip_network(ipSubnet, strict = False)
    print('\tThe 30 computers needed are equal to or less than the {} host in each subnet'.format(len(list(ipaddress.ip_network(ipSubnetAddress).hosts()))))


bitMask(2)
bitMask(13)
bitMask(5)
bitMask(11)
bitMask(9)
bitMask(10)
bitMask(4)
bitMask(14)
bitMask(6)
bitMask(8)
bitMask(12)

maskInfo('132.8.150.67/22')
maskInfo('200.16.5.74/30')
maskInfo('166.0.13.8/255.255.252.0')

bitsnHosts('10.10.10.10/255.255.240.0')
bitsnHosts('10.10.10.10/255.255.255.192')
bitsnHosts('10.10.10.10/255.255.252.0')
bitsnHosts('10.10.10.10/255.255.255.248')

subnet('10.10.10.10/16')
