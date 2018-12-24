import os
import sys
import platform

def exec_api_linux():
    os.system('python3 main/gen_api.py')
    os.system('python3 reconspider.py')

def exec_api_win():
    os.system('py -3 main/gen_api.py')
    os.system('py -3 reconspider.py')

if sys.version_info[0] > 2:
    if (platform.system() != "Windows"):
        os.system('sudo apt-get -y install python3-pip')
        os.system('sudo pip3 install python-whois clearbit shodan fullcontact.py requests')
        exec_api_linux()
    else:
        os.system('pip3 install python-whois clearbit shodan fullcontact.py requests')
        exec_api_win()
else:
    print(("Your System Python Version "+ str(sys.version_info[0]) + " isn't compatible with ReconSpider. Use Python 3.7"))
