from plugins.api import phoneapis
import requests

def Phonenumber(ph):
		print ('[+]' + ' Fetching Phonenumber Details...' + '\n')
		apikey=phoneapis()
		if apikey == "":
				print("Add NumVerify api key to plugins/api.py")
				exit()
		ph=''.join([i for i in ph if i.isdigit()])
		for api_key in apikey.split(","):
			url = ("http://apilayer.net/api/validate?access_key="+api_key+"&number="+str(ph))
			try:
				response=requests.get(url)
				if 'error' in response.json().keys():
					continue
				elif response.json()['valid']==False:
					print("Error: Invalid Mobile Number")
					return
				else:
					get=response.json()
					print("Number: "+get['number'])
					print("Type: "+get['line_type'])
					print("CountryCode: "+get['country_code'])
					print("Country: "+get['country_name'])
					print("Location: "+get['location'])
					print("Carrier: "+get['carrier'])
					print("")
					return 
			except:
				continue
		print(str(response.json()['error']['info']).split(".")[0])
				
