from requests import get


def ReverseIP(host, port):
    print ( '[+]' +  'Checking whether the Target is reachable ...' + '\n')
    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % host
    try:
        result = get(lookup).text
        print(result)
    except Exception as e:
        print('Error: Invalid IP address '+e)
