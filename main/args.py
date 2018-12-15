from modules import *
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--ip", help="Enumerate information from IP Address.")
parser.add_argument("--url", help="Enumerate information from  given Website.")
parser.add_argument("--whois", help="Gather domain registration information.")
parser.add_argument("--email", help="Gather information from email address.")
parser.add_argument("--domain", help="Gather detail of website or organization.")

args=parser.parse_args()

if args.ip:
    IP=args.ip
    ipEnum(IP)
    exit()

if args.url:
    DM=socket.gethostbyname(args.url)
    domEnum(DM)
    exit()

if args.whois:
    WH=args.whois
    domWhois(WH)
    exit()

if args.email:
    email_id=args.email
    fetchData(email_id)
    exit()

if args.domain:
    domain=args.domain
    comDetail(domain)
    exit()
