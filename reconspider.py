from main import argparse
from modules import config
import sys

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

# Checking if api keys are empty or not
if (len(config.shodan_api) < 5 or len(config.clearbit_api) < 5 or len(config.fullcontact_api) < 5):
    sys.exit("\n---------------Your Api keys are empty please ReRun the install.py file---------------\n")
else:
    banner()
