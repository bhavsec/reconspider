import requests

def HostHeader(host, port):
    if port == 80:
        port = 'http://'
    elif port == 443:
        port = 'https://'
    else:
        print("Could'nt fetch data for the given PORT")
    url = (port + host)
    headers = {'Host': 'http://evil.com'}
    response = requests.get(url, headers=headers)
    if 'evil.com' in response.headers:
        print("Vulnerable to Host Header Injection")
    else:
        print("Not Vulnerable to Host header injection")
