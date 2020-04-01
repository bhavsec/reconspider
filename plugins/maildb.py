import os

def maildb(emailaddress):
    if  ("@" and ".com") or ("@" and ".in") in emailaddress:
        os.system("h8mail -t "+emailaddress+" -o "+os.getcwd()+"/plugins/output.csv > " +os.getcwd()+"/plugins/output.log")
        f=open(os.getcwd()+"/plugins/output.csv","r")
        line=f.readlines()
        if len(line) > 1:
            for i in line:
            	print(i)
        else:
            print("Data breached is Not Compromised")
    else:
        print("Error: Invalid Email Address")
