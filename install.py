import os
import sys
import platform

def exec_api():
    os.system('python main/gen_api.py')
    os.system('python reconspider.py')

if sys.version_info[0] < 3:
    if (platform.system() != "Windows"):
        os.system('sudo apt-get install python-pip')
        os.system('sudo pip install python-whois clearbit shodan fullcontact.py requests')
        exec_api()
    else:
        os.system('C:\Python27\Scripts\pip install python-whois clearbit shodan fullcontact.py requests')
        exec_api()
else:
    print("Your System Python Version "+ str(sys.version_info[0]) + " isn't compatible with ReconSpider. Use Python 2.7")
