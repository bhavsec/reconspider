print "\n\n[+] Enter your API Keys below\n"

sd = raw_input("Enter your Shodan API Key: ").replace(" ", "")
cb = raw_input("Enter your Clearbit API Key: ").replace(" ", "")
fc = raw_input("Enter your Full Contact API Key: ").replace(" ", "")


fout = open('modules/config.py', 'w')
fout.write("shodan_api = "+"\"" + sd + "\""+"\n")
fout.write("clearbit_api = "+"\"" + cb + "\""+"\n")
fout.write("fullcontact_api = "+"\"" + fc + "\""+"\n")
fout.close()
