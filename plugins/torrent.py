import requests


def torrent(IP):

    r = requests.get("https://api.antitor.com/history/peer/?ip="+ IP +"&key=3cd6463b477d46b79e9eeec21342e4c7")
    res = r.json()
    print ( '[+]' + " Processing Torrent....." + '\n')
    if len(res)>4:
        print("IP Address: "+res['ip'])
        print("ISP: "+res['isp'])
        print("Country: "+res['geoData']['country'])
        print("Latitude: "+str(res['geoData']['latitude']))
        print("Longitude: "+str(res['geoData']['longitude'])+"\n")
        for i in res['contents']:
        	print("Category:"+i['category'])
        	print("Name:"+i['name'])
        	print("Start:" + i['startDate'])
        	print("End:" + i['endDate'])
        	print("Size:"+str(i['torrent']['size']))
        	print("")
    else:
        print("Error: Something Went Wrong")
