import sys, whois


def domWhois(WH):
    try:
        w = whois.whois(WH)
        print("\n-------------------------------------------------\n")
        print("[+] Gathering WHOIS Information from [" +str(w['whois_server']) + "] Server...\n")
        print("Domain Name: ------> "+str(w['domain_name']))
        print("Name: -------------> "+str(w['name']))
        print("Organisation: -----> "+str(w['org']))
        
        for item in w['emails']:
            print("Email: ------------> " + str(item))
        
        print("Address: ----------> "+str(w['address']))
        print("City --------------> "+str(w['city']))
        print("Country: ----------> "+str(w['country']))
        print("Zipcode: ----------> "+str(w['zipcode']))
        print("Registrar: --------> "+str(w['registrar']))
        print("Creation Date: ----> "+str(w['creation_date']))
        print("Updation Date: ----> "+str(w['creation_date']))
        print("Expiration Date: --> "+str(w['expiration_date']))

        for item in w['name_servers']:
            print("Name Server: ------> "+str(item))
        
        print("\n-------------------------------------------------\n")
    except:
        print("Try Again")
