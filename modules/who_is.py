import sys, whois


def domWhois(WH):
    try:
        w = whois.whois(WH)
        print "\n-------------------------------------------------\n"
        print "[+] Gathering WHOIS Information from [" +str(w['whois_server']) + "] Server...\n"
        print "Domain Name: ------> "+str(w['domain_name'])
        print "Name: -------------> "+str(w['name'])
        print "Organisation: -----> "+str(w['org'])
        print "Emails: -----------> "+str(w['emails'])
        print "Address: ----------> "+str(w['address'])
        print "City --------------> "+str(w['city'])
        print "Country: ----------> "+str(w['country'])
        print "Zipcode: ----------> "+str(w['zipcode'])
        print "Registrar: --------> "+str(w['registrar'])
        print "Creation Date: ----> "+str(w['creation_date'])
        print "Updation Date: ----> "+str(w['creation_date'])
        print "Expiration Date: --> "+str(w['expiration_date'])
        print "Name Server 1: ----> "+str(w.name_servers[0])
        print "Name Server 2: ----> "+str(w.name_servers[1])
        print "\n-------------------------------------------------\n"
    except:
        print "Try Again"
