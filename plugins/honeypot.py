import sys
from requests import get
from core.config import shodan_api


def honeypot(inp):
    honey = 'https://api.shodan.io/labs/honeyscore/%s?key=%s' % (inp, shodan_api)
    try:
        result = get(honey, timeout=30).text
    except Exception:
        result = None
        sys.stdout.write('\n%s No information available' % bad + '\n')
    if result and "error" not in result and "404" not in result:
            probability = str(float(result) * 10)
            print('\n[+] Honeypot Probabilty: %s%%' % (probability) + '\n')
    elif result is None:
        print("Something went Wrong")
    else:
        print("IP Not found")
