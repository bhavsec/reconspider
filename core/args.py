import socket
import argparse

from plugins.censys import censys_ip
from plugins.dnsdump import dnsmap
from plugins.honeypot import honeypot
from plugins.nslookup import nslookup
from plugins.portscan import portscan
from plugins.shodan_io import shodan_host
from plugins.shodan_io import shodan_ip
from plugins.whois import whois

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--ip', help="Enumerate information from IP Address")
parser.add_argument('-u', '--url', help="Enumerate information from  given Website")
parser.add_argument('-w', '--whois', help="Gather domain registration information")
parser.add_argument('-d', '--dnsmap', help="Map DNS records associated with the target")
parser.add_argument('-p', '--portscan', help="Discover hosts and services on a network")
parser.add_argument('-n', '--nslookup', help="Obtain domain name or IP address mapping")
parser.add_argument('-hp', '--honeypot', help="Check if it's honeypot or a real control system")

args = parser.parse_args()

if args.ip:
    IP = args.ip
    shodan_host(IP)
    censys_ip(IP)
    exit()

if args.url:
    DM = socket.gethostbyname(args.url)
    shodan_ip(DM)
    exit()

if args.whois:
    wh = args.whois
    whois(wh)
    exit()

if args.dnsmap:
    dnsmap_inp = args.dnsmap
    dnsmap(dnsmap_inp)
    exit()

if args.portscan:
    inp = args.portscan
    portscan(inp)
    exit()

if args.nslookup:
    inp = args.nslookup
    nslookup(inp)
    exit()

if args.honeypot:
    inp = args.honeypot
    honeypot(inp)
    exit()
