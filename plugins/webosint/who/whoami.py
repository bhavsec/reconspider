import whois
from pythonping import ping
import re

def whoami(target,post):
	#target=input("Enter the IP Address/Domain:")
	getweb=str(ping(target))
	ip = re.compile('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}'
                +'(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))')
	match = ip.search(getweb)
	if match:
		#target=match.group()
		w = whois.whois(target)
		print("Domain Name:"+ str(w['domain_name']))
		print("Register:"+str(w['registrar']))
		try:
			print("Whois Server:"+str(w['whois_server']))
		except Exception as e:
			print(e)
		print("Server:"+str(w['name_servers']))
		print("Emails:"+str(w['emails']))
		try:
			print("Organisation:"+str(w['org']))
		except Exception as e:
			print("Organisation:"+str(w['organization']))
			print(e)
		try:
			print("Address:"+str(w['address']))
			print("City:"+str(w['city']))
			print("State:"+str(w['state']))
			print("Zipcode:"+str(w['zipcode']))
		except Exception as e:
			print(e)
		print("Country:"+str(w['country']))
