import requests
requests.packages.urllib3.disable_warnings()

def header(target,port):
	if port == 80:
		port="http://"
	elif port == 443:
		port="https://"
	else:
		print("Could'nt fetch data for the given PORT")
		exit()
	print ('\n' + '[+]' + ' Headers :' + '\n')
	rqst = requests.get(port+target, verify=True, timeout=10)
	for k, v in rqst.headers.items():
		print ('[+]' + ' {} : '.format(k) + v)
