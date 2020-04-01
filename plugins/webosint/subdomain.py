import requests

def SubDomain(host, port):
    print ('[+]' +  'Fetching Subdomains of Target...' + '\n')
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'

    params = {'apikey':'1af37bfeb7b1628ba10695fb187987a6651793e37df006a5cdf8786b0e4f6453','domain':host}

    response = requests.get(url, params=params)

    subdomains = response.json()

    for x in subdomains['domain_siblings']:
        print(x)
