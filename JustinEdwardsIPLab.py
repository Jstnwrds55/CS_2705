import ipaddress


def ipAddress(ip, outputs):

    ipInterface = ipaddress.ip_interface(ip)
    ipNetwork = ipInterface.network

    if outputs == 'networkFirstUsable':
        print('What is the first address of a block of classless addresses if one of the addresses is ', ip + '?')
        print('{} is the network address'.format(ipaddress.ip_network(ipNetwork).network_address))
        print('{} is the first usable address'.format((ipaddress.ip_network(ipNetwork).network_address) + 1), '\n')

    elif outputs == 'totalUsable':
        print('Find the number of addresses in a block of classless addresses if one of the addresses is', ip + '.')
        print('{} is the total number of addresses available'.format(ipaddress.ip_network(ipNetwork).num_addresses))
        print('{} is the total number of usable addresses'.format((ipaddress.ip_network(ipNetwork).num_addresses) - 2),
              '\n')

    elif outputs == 'broadcastUsable':
        print('What is the last address of a block of classless addresses if one of the addresses is', ip + '?')
        print('{} is the broadcast address'.format(ipaddress.ip_network(ipNetwork).broadcast_address))
        print('{} is the last usable address'.format((ipaddress.ip_network(ipNetwork).broadcast_address) - 1), '\n')

    elif outputs == "prefixLength":
        print(list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff=2)))


ipAddress('192.168.2.76/28', 'networkFirstUsable')
ipAddress('192.168.2.76/9', 'networkFirstUsable')
ipAddress('192.168.2.137/27', 'networkFirstUsable')

ipAddress('101.10.2.8/15', 'totalUsable')
ipAddress('101.10.2.8/29', 'totalUsable')

ipAddress('192.168.2.137/27', 'broadcastUsable')
ipAddress('110.10.2.55/30', 'broadcastUsable')





