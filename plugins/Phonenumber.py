from plugins.api import phoneapis
<<<<<<< HEAD
import requests
=======
import 
>>>>>>> ebe8448227c7bdd9dd40c4dc884d9e056cdd5634

def Phonenumber(ph):
    print ('[+]' + ' Fetching Phonenumber Details...' + '\n')
    api_key=phoneapis()
    if api_key == "":
        print("Add you phoneapis api key to src/api.py")
        exit()
    url = ("http://apilayer.net/api/validate?access_key="+api_key+"&number="+str(ph))
    response=requests.get(url)
    if "91" not in str(ph):
        print("Error: CountryCode is missing")
    else:
        if response.status_code ==200:
            get=response.json()
            print("Number: "+get['number'])
            print("Type: "+get['line_type'])
            print("CountryCode: "+get['country_code'])
            print("Country: "+get['country_name'])
            print("Location: "+get['location'])
            print("Carrier: "+get['carrier'])
            print("")
        else:
            print("Error: Invalid Mobile Number")
