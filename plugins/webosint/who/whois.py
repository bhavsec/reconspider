import requests

def whois_more(IP):
        result = requests.get('http://api.hackertarget.com/whois/?q=' + IP).text
        print('\n'+ result + '\n')
