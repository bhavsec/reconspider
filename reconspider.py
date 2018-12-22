from main import argparse


def banner():
    print """
__________                               _________       __     ___            
\______   \ ____   ____  ____   ____    /   _____/_____ |__| __| _/___________ 
 |       _// __ \_/ ___\/  _ \ /    \   \_____  \\\____ \|  |/ __ |/ __ \_  __ \\
 |    |   \  ___/\  \__(  <_> )   |  \  /        \  |_> >  / /_/ \  ___/|  | \/
 |____|_  /\___  >\___  >____/|___|  / /_______  /   __/|__\____ |\___  >__|   
        \/     \/     \/           \/          \/|__|           \/    \/       

                      developer: https://bhavkaran.com


usage: python reconspider.py [OPTIONS]

OPTIONS:


  --ip                  Enumerate information from IP Address.
  --url                 Enumerate information from given Website.
  --whois               Gather domain registration information.
  --email               Gather information from email address.
  --domain              Gather detail of website or organization.
  --help                Show this help message and exit.
    """


banner()
