import os
import platform

if (platform.system() != "Windows"):
    os.system('apt-get install python-pip')
    os.system('pip install python-whois')
    os.system('pip install clearbit')
    os.system('pip install shodan')
    os.system('pip install fullcontact.py')
    os.system('pip install requests')
    os.system('mv modules/config_sample.py modules/config.py')
else:
    os.system('C:\Python27\Scripts\pip install python-whois')
    os.system('C:\Python27\Scripts\pip install clearbit')
    os.system('C:\Python27\Scripts\pip install shodan.py')
    os.system('C:\Python27\Scripts\pip install fullcontact')
    os.system('C:\Python27\Scripts\pip install requests')
    os.system('mv modules/config_sample.py modules/config.py')
