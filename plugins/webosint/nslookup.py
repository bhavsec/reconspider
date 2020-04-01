from requests import get

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def nsLookup(host, port):
    print ( '[+]' + 'Fetching Details...' + '\n')
    result = get('http://api.hackertarget.com/dnslookup/?q=' + host).text
    print(result)
