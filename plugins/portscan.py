import sys
from requests import get


def portscan(inp):
    result = get('http://api.hackertarget.com/nmap/?q=' + inp).text
    print('\n' + result + '\n')
