print("\n\n[+] Enter your API Keys below\n")

sd = input("Enter your Shodan API Key: ").replace(" ", "")
cb = input("Enter your Clearbit Secret API Key: ").replace(" ", "")
fc = input("Enter your Full Contact API Key: ").replace(" ", "")


fout = open("modules/config.py", "w")
fout.write("shodan_api = " + '"' + sd + '"' + "\n")
fout.write("clearbit_api = " + '"' + cb + '"' + "\n")
fout.write("fullcontact_api = " + '"' + fc + '"' + "\n")
fout.close()
