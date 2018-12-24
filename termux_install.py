import os

os.system('pkg install python2')
os.system('pip2 install python-whois clearbit shodan fullcontact.py requests')
os.system('python2 main/gen_api.py')
os.system('python2 reconspider.py')
