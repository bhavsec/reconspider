import sys
from requests import get
from core.config import shodan_api


def honeypot(inp):
    honey = 'https://api.shodan.io/labs/honeyscore/%s?key=%s' % (inp, shodan_api)
    try:
        result = get(honey).text
    except:
        result = None
        sys.stdout.write('\n%s No information available' % bad + '\n')
    if "error" in result or "404" in result:
        print("IP Not found")
        return
    elif result:
            probability = str(float(result) * 10)
            print('\n[+] Honeypot Probabilty: %s%%' % (probability) + '\n')
    else:
        print("Something went Wrong")
