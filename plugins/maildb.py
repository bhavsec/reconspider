import requests

def maildb(emailaddress):
    if  ("@" and ".com") or ("@" and ".in") in emailaddress:
        req=requests.get("https://api.hunter.io/v2/domain-search?domain="+emailaddress+"&api_key=9f189e87e011a1d2f3013ace7b14045dec60f62c")
        j=req.json()
        print("[+] Breaching from "+emailaddress+"...\n")
        for i in range(len(j['data']['emails'])):
            print("Email ID   :",j['data']['emails'][i]['value'])
            print("First Name :",j['data']['emails'][i]['first_name'])
            print("Last Name  :",j['data']['emails'][i]['last_name'])
            if j['data']['emails'][i]['position']!=None:
                print("Position   :",j['data']['emails'][i]['position'])
            if j['data']['emails'][i]['linkedin']!=None:
                print("Linkedin   :",j['data']['emails'][i]['linkedin'])
            if j['data']['emails'][i]['twitter']!=None:
                print("Twitter    :",j['data']['emails'][i]['twitter'])
            print()
    else:
        print("Error: Invalid Email Address")
