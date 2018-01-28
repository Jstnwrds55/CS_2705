import ipaddress


def ipAddress(ip, outputs):

    ipInterface = ipaddress.ip_interface(ip)
    ipNetwork = ipInterface.network

    print(ipNetwork)

    if outputs == 'networkFirstUsable':
        print('What is the first address of a block of classless addresses if one of the addresses is ', ip + '?')
        print('Network Address: {}'.format(ipaddress.ip_network(ipNetwork).network_address))
        print('First Usable Address: {}'.format((ipaddress.ip_network(ipNetwork).network_address) + 1), '\n')

    elif outputs == 'totalUsable':
        print('Find the number of addresses in a block of classless addresses if one of the addresses is', ip + '.')
        print('Total Addresses Available: {}'.format(ipaddress.ip_network(ipNetwork).num_addresses))
        print('Total Usable Addresses: {}'.format((ipaddress.ip_network(ipNetwork).num_addresses) - 2),
              '\n')

    elif outputs == 'broadcastUsable':
        print('What is the last address of a block of classless addresses if one of the addresses is', ip + '?')
        print('Broadcast Address: {}'.format(ipaddress.ip_network(ipNetwork).broadcast_address))
        print('Last Usable Address: {}'.format((ipaddress.ip_network(ipNetwork).broadcast_address) - 1), '\n')

    elif outputs == "prefixLength":
        print('An organization is granted a block; one address is', ip +'. The organization needs 10 subnets. What is the subnet prefix length?')
        print('Prefix Length: {}\n'.format(ipaddress.ip_network(ipNetwork).prefixlen))

    elif outputs == 'maxSubAddress':
        print('An organization is granted a block; one address is 110.10.10.64/25. If the subnet prefix length is /28, what is the maximum number of subnets and how many addresses in each subnet?')
        print('{} subnets with {} addresses in each subnet.'.format(2*2*2, ipaddress.ip_network(ipNetwork).num_addresses), '\n')

    elif outputs == 'totalAddress':
        print('An organization is granted a block of classless addresses with the starting address: ' + ip + '. How many addresses are granted?')
        print('Total Addresses Available: {}'.format(ipaddress.ip_network(ipNetwork).num_addresses), '\n')


ipAddress('192.168.2.76/28', 'networkFirstUsable')
ipAddress('192.168.2.76/9', 'networkFirstUsable')
ipAddress('192.168.2.137/27', 'networkFirstUsable')

ipAddress('101.10.2.8/15', 'totalUsable')
ipAddress('101.10.2.8/29', 'totalUsable')

ipAddress('192.168.2.137/27', 'broadcastUsable')
ipAddress('110.10.2.55/30', 'broadcastUsable')

ipAddress('110.10.10.64/24', 'prefixLength')

ipAddress('110.10.10.64/28', 'maxSubAddress')

ipAddress('156.78.51.24/25', 'totalAddress')
ipAddress('156.78.51.24/30', 'totalAddress')
ipAddress('166.25.132.0/3', 'totalAddress')





