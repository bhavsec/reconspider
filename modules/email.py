from fullcontact import FullContact
from config import fullcontact_api
from person import perDetail
import json
fc = FullContact(fullcontact_api)


def fetchData(email_id):
    person = fc.person(email=email_id)
    data = person.json()
    try:
        print "\n-------------------------------------------------\n"
        print "[+] Gathering Personal Information from [FullContact]\n"
        print "Full Name: ----> "+data['contactInfo']['fullName']
        print "Gender: -------> "+str(data['demographics']['gender'])
        print "State: --------> "+str(data['demographics']['locationDeduced']['state']['name'])
        print "Country: ------> "+str(data['demographics']['locationDeduced']['country']['name'])
        for u in data['contactInfo']['websites']:
            print "Website: ------> "+u['url']
        
    except:
        print "Unavailable"

    try:
        print "\n\n[+] Gathering Employment Details from [FullContact]\n"
        for org in data['organizations']:
            print "Organisation Name: "+org['name']+" "+"\nJob Title: "+" "+org['title']+" "+"\nStart date: "+" "+org['startDate']+"\n"
        
    except:
        print "Unavailable"


    try:
        print "\n\n[+] Gathering Social Accounts from [FullContact]\n"
        for soc in data['socialProfiles']:
            print ""+soc['typeName'] + ": " +soc['url']
        print "\n-------------------------------------------------\n"
    
        print perDetail(email_id)
    
    except:
        print "Unavailable"
        print "\n-------------------------------------------------\n"

        print perDetail(email_id)
