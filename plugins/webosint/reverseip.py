from requests import get

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def ReverseIP(host, port):
    print ( '[+]' +  'Checking whether the Target is reachable ...' + '\n')
    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % host
    try:
        result = get(lookup).text
        print(result)
    except:
        print(R+'Error: Invalid IP address')
