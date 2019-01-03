import sys

def banner():
       return("""
__________                               _________       __     ___            
\______   \ ____   ____  ____   ____    /   _____/_____ |__| __| _/___________ 
 |       _// __ \_/ ___\/  _ \ /    \   \_____  \\\____ \|  |/ __ |/ __ \_  __ \\
 |    |   \  ___/\  \__(  <_> )   |  \  /        \  |_> >  / /_/ \  ___/|  | \/
 |____|_  /\___  >\___  >____/|___|  / /_______  /   __/|__\____ |\___  >__|   
        \/     \/     \/           \/          \/|__|           \/    \/       

                      developer: https://bhavkaran.com


ENTER 0 - 7 TO SELECT OPTIONS

1. IP                Enumerate  information  from  IP Address
2. URL               Gather  information  about given Website
3. WHOIS             Gather domain  registration  information
4. DNS MAP           Map DNS  records associated  with target
5. PORT SCAN         Discover hosts and services on a network
6. NS LOOKUP         Obtain domain name or IP address mapping
7. HONEYPOT          Check if it's honeypot or a real  system
8. UPDATE            Update ReconSpider to its latest version

0. EXIT              Exit from  ReconSpider  to your terminal
       """)

if sys.version_info[0] > 2:
       try:
              print(banner())
              from core import repl_prompt

       except ModuleNotFoundError:
              print('\nSeems like you haven\'t installed Requirements, Please install using: python setup.py install')
              quit()
else:
       try:
              print(banner())
              from core import repl_prompt
       
       except ImportError:
              print('\nSeems like you haven\'t installed Requirements, Please install using: python setup.py install')
              quit()
