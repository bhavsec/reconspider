import shodan
from config import shodan_api
api = shodan.Shodan(shodan_api)


def ipEnum(IP):
    try:
        host = api.host(IP)
        print "\n-------------------------------------------------\n"
        print "[+] Gathering IP Address Information from [shodan]\n"
        print "IP Address ----> "+str(host['ip_str'])
        print "Country -------> "+str(host['country_name'])
        print "City ----------> "+str(host['city'])
        print "Organization --> "+str(host['org'])
        print "ISP -----------> "+str(host['isp'])
        print "Open ports ----> "+str(host['ports'])
        print "\n-------------------------------------------------\n"
    except:
        print "Unavailable"
        print "\n-------------------------------------------------\n"
