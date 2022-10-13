import ipaddress
cidrx = '185.117.0.0/21'
set1 = ipaddress.ip_network(cidrx)
ip_list=[str(ip) for ip in set1]
for ipv4 in ip_list:
    print(ipv4)