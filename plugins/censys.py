import json
from requests import get


def censys_ip(IP):
    try:
        dirty_response = get('https://censys.io/ipv4/%s/raw' % IP).text
        clean_response = dirty_response.replace('&#34;', '"')
        x = clean_response.split('<code class="json">')[1].split('</code>')[0]
        censys = json.loads(x)

        print("\n[+] Gathering Location Information from [censys]\n")
        print("Country -------> "+str(censys["location"]["country"]))
        print("Continent -----> "+str(censys["location"]["continent"]))
        print("Country Code --> "+str(censys["location"]["country_code"]))
        print("Latitude ------> "+str(censys["location"]["latitude"]))
        print("Longitude -----> "+str(censys["location"]["longitude"]))
    except:
        print("Unavailable")
