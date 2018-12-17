import os
import platform

if (platform.system() != "Windows"):
    os.system('apt-get install python-pip')
    os.system('pip install python-whois clearbit shodan fullcontact.py requests')
else:
    os.system('C:\Python27\Scripts\pip install python-whois clearbit shodan fullcontact.py requests')


os.system('python main/gen_api.py')
os.system('python reconspider.py')
