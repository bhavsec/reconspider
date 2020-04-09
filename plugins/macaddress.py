import requests

def MacAddressLookup(mac):
    url = ("https://macvendors.co/api/" + mac)
    response=requests.get(url)
    result=response.json()
    if result["result"]:
        final=result['result']
        print("Company:" + final["company"])
        print("Address:" + final["address"])
        print("Country:" + final["country"])
        print("")
    else:
        print("Error: Something Went Wrong")
