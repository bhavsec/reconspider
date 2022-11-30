import requests
import gmplot
from plugins.api import ipstack
import webbrowser
import re
from plugins.api import gmap
from ipaddress import *
from plugins.webosint.who.whois import *

api_key = ipstack()
if api_key == "" :
    print("Add you ipstack api key to plugins/api.py")
    exit()
if gmap() == "" :
    print("Add you Google Heatmap api key to plugins/api.py")
    exit()

def IPHeatmap():
    print('''
    1) Trace single IP
    2) Trace multiple IPs''')
    choice = input("OPTIONS >> ")

    if choice == '1':
        IP = input("Enter the IP : ")
        read_single_IP(IP)
    elif choice == '2':
        IP_file = input("Enter the IP File Location : ")
        read_multiple_IP(IP_file)
    else:
        print("\nError: Please choose an appropriate option")

def read_single_IP(IP):
    print ('[+]' + "Processing IP: %s ..." %IP + '\n')
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",IP):
        print("Invalid IP Address")
        IPHeatmap()
    lats = []
    lons = []
    r = requests.get("http://api.IPstack.com/" + IP + "?access_key=" + api_key)
    response = r.json()
    print('')
    print("IP :"+response['ip'])
    print("Location : " + response['region_name'])
    print("Country : " +response['country_name'])
    print("Latitude :"+" {latitude}".format(**response))
    print("Longitude :"+" {longitude}".format(**response))
    if input("Want More Whois Details (Y/N): ") in ("Y","y"):
        whois_more(IP)
    if response['latitude'] and response['longitude']:
        lats = response['latitude']
        lons = response['longitude']
    maps_url = "https://maps.google.com/maps?q=%s,+%s" % (lats, lons)
    print("")
    openWeb = input("Open GPS location in web broser? (Y/N) ")
    if openWeb.upper() == 'Y':
        webbrowser.open(maps_url, new=2)
    else:
        pass

def read_multiple_IP(IP_file):
    lats = []
    lons = []
    try:
        f = open(IP_file, "r")
        f1 = f.readlines()
        print ('[+]' + " Processing....." + '\n')
        for line in f1:
            IP=re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",line)
            IP=IP.group()
            r = requests.get("http://api.IPstack.com/" + IP + "?access_key=" + api_key)
            response = r.json()
            if response['latitude'] and response['longitude']:
                lats.append(response['latitude'])
                lons.append(response['longitude'])
        heat_map(lats,lons)
    except IOError:
        print("ERROR : File Does not Exist\n")
        IPHeatmap()


def heat_map(lats,lons):
    gmap3 = gmplot.GoogleMapPlotter(20.5937, 78.9629, 5)
    gmap3.heatmap(lats,lons)
    gmap3.scatter(lats,lons, '#FF0000', size=50, marker=False)
    gmap3.plot(lats,lons, 'cornflowerblue', edge_width = 3.0)
    save_location = input("Enter the location to save file : ")
    gmap3.apikey = gmap()
    location = save_location + "/heatmap.html"
    gmap3.draw(location)
    print("Heatmap saved at " + location)
    openWeb = input("Open Heatmap in web broser? (Y/N) : ")
    if openWeb.upper() == 'Y':
        webbrowser.open(url=("file:///"+location))
    else:
        pass
