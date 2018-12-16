import os
import platform

if (platform.system() != "Windows"):
    os.system('apt-get install python-pip')
    os.system('pip install python-whois clearbit shodan fullcontact.py requests')
    os.system('mv modules/config_sample.py modules/config.py')
    os.system('clear && python reconspider.py')
else:
    os.system('C:\Python27\Scripts\pip install python-whois clearbit shodan fullcontact.py requests')
    os.system('cd modules && ren config_sample.py config.py && cd..')
    os.system('cls && python reconspider.py')
