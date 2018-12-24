import sys
import os

if sys.version_info[0] > 2:
    os.system('pkg install python3')
    os.system('pip3 install python-whois clearbit shodan fullcontact.py requests')
    os.system('python3 main/gen_api.py')
    os.system('python3 reconspider.py')
else:
    print(("Your System Python Version "+ str(sys.version_info[0]) + " isn't compatible with ReconSpider. Use Python 3.7"))