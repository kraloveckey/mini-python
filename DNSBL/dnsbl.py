# DNSBL is DNS blacklist, that is, black lists that are stored on servers using DNS structure. 
# From the name itself it is clear that these lists are designed so that the postal servers check them, and, on the basis of the received
# data formed a reputation as an address or host. Getting on these lists is easy, but getting out is already harder. 
# Here, we can say, it all depends on who forms the rules for adding address to them.
# And if the moon coincided with Saturn, it may turn out that your white and fluffy domain will fall into it with very great ease.
# For example, you can get for the following reasons: suspicious activity of a mail server; incorrect setting of server configuration;
# customer complaints; proxy and many other reasons. There are a lot of black host lists. 
# But, it’s not about how to delete the address from the black list, but about how to check if your domain address has got there using Python.

import re
import socket
import dns
from dns import resolver
from colorama import Fore
from colorama import init
from ipaddress import ip_network, ip_address
from requests import get, exceptions

init()

# Verification of the address in the Cloudflare range.
# This check is done in order not to waste time and torment the DNS server. 
# However, to check or not, it all depends on the user. But about whether the address is included in the range must be reported.
# Create the ip_in_range (ip, addr) function, which at the entrance accepts the IP address and the range of Cloudflare addresses, checks, 
# whether the address is contained in the range and returns depending on this True or False. 
# To perform this check, we will use the ipaddress library and its ip_address and ip_network functions. 
# Using the first, we translate the line to the address, and with the help of the second we create a range of addresses from the transmitted address with the specified range.
def ip_in_range(ip, addr):
    if ip_address(ip) in ip_network(addr):
        return True
    return False

# Download the list of the Cloudflare address ranges and start the IP address checking function.
# At the next stage, we need a second function, which is also to check the address of Cloudflare. 
# Here, at the entrance, the function receives an IP address. Then it loads the list of address ranges and puts them in the cycle in a list_addr list pre-created for this. 
# This list is not empty, first one range has already been added to it, since this range is not when loaded. 
# But when checking the address using Whois, it is suddenly located. Then we start another cycle in which we run along the list 
# the formed address ranges and transfer them to the address verification function. If the address is in the ranges, we return True, if not - False.
def cloudf_detect(ip):
    list_addr = ["104.16.0.0/12"]

    url = 'https://www.cloudflare.com/ips-v4'
    req = get(url=url)

    for adr in req.text.split("\n"):
        list_addr.append(adr)

    for addr in list_addr:
        detect = ip_in_range(ip, addr)
        if detect:
            return True
    return False

# Obtaining an external IP address of a computer.
# We make a request using requests to the api.ipify.org, and an external IP address arrives in response. 
# If, for some reason, the connection with this site doesn't occur, we process the exception and return localhost.
def public_ip():
    try:
        return get('https://api.ipify.org/').text
    except exceptions.ConnectionError:
        return '127.0.0.1'

# Download the DNSBL list, obtaining information about the presence of an address in the lists.
# At the entrance, the function takes an IP address, even if the presence of a domain in black lists is checked. 
# СWe create a dictionary in which we will put the name of the list in which there is an address and the contents of the "TXT" field, in which, mainly, 
# the address is indicated where you can apply for the details if the address is suddenly found here. After we get a list of DNSBL in which we will check the address. 
# For the list, a dnsbl.txt file has been created, in which the address is located, the dnsbl.txt file is located next to the dnsbl.py script.
# A cycle is launched at these address lines, where each line is crossed and a request is formed. The request is formed in the reverse order,
# that is, the reverse should turn out: 2.0.0.127.dbl.spamhaus.org. Therefore, we break the line into parts in the lines, make a reverse and collect again. 
# The second parameter for assembling the request is the address of the black list from the line.
def dns_bl_check(ip):
    print(Fore.YELLOW + '\n- Checking black lists\n')
    bad_dict = dict()
    with open('dnsbl.txt', 'r') as file:
        req = file.readlines()
    for serv in req:
        req = f"{'.'.join(reversed(ip.split('.')))}.{serv.strip()}"
        try:
# Now we create a resolver, set a timeout for a request, as well as its lifetime.
            resolv = dns.resolver.Resolver()
            resolv.timeout = 5
            resolv.lifetime = 5
# We make requests to records of type "A" and "txt". We get data from them. If the data is obtained, then print the line with the server,
# from which they received data and the result of the request, in this case BAD, since the desired address was found, which means that it is contained on the black list. 
# Next, we determine the pattern for the regular expression, with which we will look for links in the answers TXT. 
# If there aren't links, we write that there is nothing. And finally, add the found in the dictionary. 
# That is, we add the server name where we were looking for, the result of the answer by type A, and the link found or not found to the details.
            resp = resolv.resolve(req, 'A')
            resp_txt = resolv.resolve(req, 'TXT')
            print(Fore.RED + f'{serv.strip():30}: [BAD]')
            pattern = '(?:https?:\/\/)?(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)(?:\/[\w\.]*)*\/?'
            find = re.findall(pattern, str(resp_txt[0]))
            if len(find) == 0:
                find = ['No address']
            bad_dict.update({serv.strip(): f'{resp[0]} {find[0]}'})
# We process the exceptions that will arise when making requests. There can be more, but basically, most often these. 
# The first exception arises when there are no records. It is necessary in order to print, that on this server with the IP address everything is OK. 
# And the next two, this is an exception that arises when the response time expires and when there is no answer from the server.
        except dns.resolver.NXDOMAIN:
            print(Fore.GREEN + f'{serv.strip():30}: [OK]')
        except (dns.resolver.LifetimeTimeout, dns.resolver.NoAnswer):
            continue
# Further have processing what we got. If the dictionary, in which the found recordings found are empty, joyfully inform the user about this. If not, we display its contents.
    if len(bad_dict) > 0:
        len_str = len(f'IP address: "{ip.upper()}" Discovered on black lists!')
        print(Fore.BLUE + f'\nIP address: {ip.upper()} Discovered on black lists!\n{"*"*len_str}')
        for bad in bad_dict:
            print(f' - {Fore.YELLOW + bad:30} : {Fore.RESET +bad_dict[bad]}')
    else:
        print(Fore.GREEN + '\n[+] IP address on black lists was not detected')

# Obtaining user input. Launch of the check for the address of the CloudFlare address.  Launching the check of the address in the DNSBL.
# Here, for starters, we inform the user his external IP address. Then we request an address or domain for verification. If he wants to go out, he can enter 'x'. 
# After we get an IP address, as the user can enter the domain name. In the event of an error of receiving the address, we complete the script.
# After the address is received, we launch the check if the received IP address for Cloudflare is hidden. And if so, then we offer the user an alternative,
# check or not check. In case of verification, start the function. If not, we just return to the user menu. 
# And if the addresses for Cloudflare aren't found, just start the check function.
def main():
    print(Fore.CYAN + f'\n- Your external IP address: {public_ip()}')
    addr_input = input('- Enter the IP address or domain for verification\n Enter for exit "x"\n  >>> ')
    if addr_input.lower() == "x":
        exit(0)
    ip = ''
    try:
        ip = socket.gethostbyname(addr_input)
    except socket.gaierror:
        print(Fore.RED + '\n - Failed to get IP addresses')
        exit(0)
    if cloudf_detect(ip):
        print(Fore.RED + f'\n[!] ATTENTION! Cloudflare address was found: {ip}')
    dns_bl_check(ip)

if __name__ == "__main__":
    main()