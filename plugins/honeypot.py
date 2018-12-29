import sys
from requests import get
from core.config import shodan_api
from core.colors import bad, info, red, green, end


def honeypot(inp):
    honey = 'https://api.shodan.io/labs/honeyscore/%s?key=%s' % (inp, shodan_api)
    try:
        result = get(honey).text
    except:
        result = None
        sys.stdout.write('\n%s No information available' % bad + '\n')
    if result:
        if float(result) < 0.5:
            color = green
        else:
            color = red
        probability = str(float(result) * 10)
        print('\n%sHoneypot Probabilty: %s%s%%%s' % (info, color, probability, end) + '\n')
