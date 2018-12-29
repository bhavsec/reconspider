from core import argparse

print("""
__________                               _________       __     ___            
\______   \ ____   ____  ____   ____    /   _____/_____ |__| __| _/___________ 
 |       _// __ \_/ ___\/  _ \ /    \   \_____  \\\____ \|  |/ __ |/ __ \_  __ \\
 |    |   \  ___/\  \__(  <_> )   |  \  /        \  |_> >  / /_/ \  ___/|  | \/
 |____|_  /\___  >\___  >____/|___|  / /_______  /   __/|__\____ |\___  >__|   
        \/     \/     \/           \/          \/|__|           \/    \/       

                      developer: https://bhavkaran.com


usage: python reconspider.py [OPTIONS]

OPTIONS:

--ip       , -i     Enumerate information from IP Address
--url      , -u     Gather information about given Website
--whois    , -w     Gather domain registration information
--dnsmap   , -d     Map DNS records associated with the target
--portscan , -p     Discover hosts and services on a network
--nslookup , -n     Obtain domain name or IP address mapping
--honeypot , -hp    Check if it's honeypot or a real control system
""")
