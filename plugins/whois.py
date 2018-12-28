import sys
from requests import get


def whois(wh):
    url = wh
    result = get('http://api.hackertarget.com/whois/?q=' + url).text
    print('\n'+ result + '\n')