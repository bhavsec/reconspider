import shodan
from core.config import shodan_api

api = shodan.Shodan(shodan_api)


def shodan_host(IP):
    try:
        host = api.host(IP)
        print("\n[+] Gathering IP Address Information from [shodan]\n")
        print("IP Address ----> " + str(host['ip_str']))
        print("Country -------> " + str(host['country_name']))
        print("City ----------> " + str(host['city']))
        print("Organization --> " + str(host['org']))
        print("ISP -----------> " + str(host['isp']))
        print("Open ports ----> " + str(host['ports']))
    except:
        print("Unavailable")


def shodan_ip(IP):
    try:
        host = api.host(IP)
        print("\n[+] Gathering Domain Information from [shodan]\n")
        print("IP Address ----> " + str(host['ip_str']))
        print("Country -------> " + str(host['country_name']))
        print("City ----------> " + str(host['city']))
        print("Organization --> " + str(host['org']))
        print("ISP -----------> " + str(host['isp']))
        print("Open ports ----> " + str(host['ports']))
    except:
        print("Unavailable")
