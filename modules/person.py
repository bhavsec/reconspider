from config import clearbit_api
import requests
import json
import clearbit
import os
clearbit.key=clearbit_api

def perDetail(email_id):
    try:
        person=clearbit.Person.find(email=email_id,stream=True)
        if person != None:
            
            print "\n[+] Gathering Personal Information from [clearbit]\n"
            print "First Name: ---------> "+str(person['name']['givenName'])
            print "Last Name: ----------> "+str(person['name']['familyName'])
            print "Full Name: ----------> "+str(person['name']['fullName'])
            print "Description: --------> "+str(person['bio'])
            print "Website: ------------> "+str(person['site'])


            print "\n[+] Gathering Location Information from [clearbit]\n"
            print "City:----------------> "+str(person['geo']['city'])
            print "State: --------------> "+str(person['geo']['state'])
            print "Country: ------------> "+str(person['geo']['country'])
            print "Full Location: ------> "+str(person['location'])
            print "Time Zone: ----------> "+str(person['timeZone'])
            print "Latitude: -----------> "+str(person['geo']['lat'])
            print "Longitude: ----------> "+str(person['geo']['lng'])


            print "\n[+] Gathering Employment Information from [clearbit]\n"
            print "Company Name: -------> "+str(person['employment']['name'])
            print "Title: --------------> "+str(person['employment']['title'])
            print "Role: ---------------> "+str(person['employment']['role'])
            print "Seniority: ----------> "+str(person['employment']['seniority'])
            print "Domain: -------------> "+str(person['employment']['domain'])


            print "\n[+] Gathering Social Accounts Information from [clearbit]\n"
            print "Facebook: -----------> "+str(person['facebook']['handle'])
            print "Github: -------------> "+str(person['github']['handle'])
            print "Twitter: ------------> "+str(person['twitter']['handle'])
            print "LinkedIn: -----------> "+str(person['linkedin']['handle'])
            print "Google Plus: --------> "+str(person['googleplus']['handle'])
            print "\n-------------------------------------------------\n"
        else:
            print "No information"
    except:
        print "Try Again"
