import os
def whois_more(IP):
    os.system("whois "+IP+" > output.txt")
    f=open("output.txt","r")
    f1=f.readlines()
    for line in f1:
    	if "%" not in line and line.strip():
            print(line)
