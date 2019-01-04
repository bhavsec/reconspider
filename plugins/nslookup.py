from requests import get


def nslookup(inp):
    result = get('http://api.hackertarget.com/dnslookup/?q=' + inp).text
    print('\n' + result)
