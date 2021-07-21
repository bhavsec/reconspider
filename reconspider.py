import sys

def banner():
       return ("""
__________                               _________       __     ___
\______   \ ____   ____  ____   ____    /   _____/_____ |__| __| _/___________
 |       _// __ \_/ ___\/  _ \ /    \   \_____  \\\____ \|  |/ __ |/ __ \_  __ \\
 |    |   \  ___/\  \__(  <_> )   |  \  /        \  |_> >  / /_/ \  ___/|  | \/
 |____|_  /\___  >\___  >____/|___|  / /_______  /   __/|__\____ |\___  >__|
        \/     \/     \/           \/          \/|__|           \/    \/
""")
def menu():
    return ("""
ENTER 0 - 13 TO SELECT OPTIONS

1.  IP                           Enumerate  information  from  IP Address
2.  DOMAIN                       Gather  information  about  given DOMAIN
3.  PHONENUMBER                  Gather  information  about   Phonenumber
4.  DNS MAP                      Map DNS  records associated  with target
5.  METADATA                     Extract all metadata of  the  given file
6.  REVERSE IMAGE SEARCH         Obtain domain name or IP address mapping
7.  HONEYPOT                     Check if it's honeypot or a real  system
8.  MAC ADDRESS LOOKUP           Obtain information about give Macaddress
9.  IPHEATMAP                    Draw  out  heatmap  of  locations  of IP
10. TORRENT                      Gather torrent download  history  of  IP
11. USERNAME                     Extract Account info. from social  media
12. IP2PROXY                     Check whether  IP  uses  any VPN / PROXY
13. MAIL BREACH                  Checks given domain  has  breached  Mail
99. UPDATE                       Update ReconSpider to its latest version

0. EXIT                         Exit from  ReconSpider  to your terminal
       """)

if __name__ == '__main__':
    if sys.version_info[0] > 2:
           try:
                  print(banner())
                  from core import repl_prompt
           except ModuleNotFoundError:
                  print('\nSeems like you haven\'t installed Requirements or You are not using python3 version, Please install using: python3 setup.py install')
                  quit()
    else:
           try:
                  from core import repl_prompt
           except ImportError:
                  print('\nSeems like you haven\'t installed Requirements or You are not using python3 version,, Please install using: python3 setup.py install')
                  quit()
