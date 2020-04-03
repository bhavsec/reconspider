# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from plugins.censys import censys_ip
from plugins.dnsdump import dnsmap
from plugins.honeypot import honeypot
from plugins.shodan_io import shodan_host
from plugins.domain import domain
from plugins.Phonenumber import Phonenumber
from plugins.reverseimagesearch import reverseimagesearch
from plugins.metadata import gps_analyzer
from plugins.macaddress import MacAddressLookup
from plugins.ipaddress import IPHeatmap
from plugins.torrent import torrent
from plugins.proxy import ip2Proxy
from plugins.maildb import maildb
from plugins.Username import user
from core.updater import update
from prompt_toolkit import prompt


def repl():  # Read–eval–print loop
    while 1:
        user_input = prompt("\nReconspider >> ")
        if len(user_input)==0:
            print("ENTER 1 - 13 TO SELECT OPTIONS")
            continue
        try:
            choice = int(user_input)
        except ValueError:
            print("ENTER 1 - 7 TO SELECT OPTIONS")
            continue

        if choice == 1:
            while 1:
                ip = prompt("IP >> ")
                break
            shodan_host(ip)
            censys_ip(ip)
            continue

        elif choice == 2:
            while 1:
                host = input("HOST (URL / IP) >> ")
                port = int(input("PORT >> "))
                break
            domain(host,port)
            continue

        elif choice == 3:
            while 1:
                ph = prompt("PHONE NUMBER (919485247632) >> ")
                break
            Phonenumber(ph)
            continue

        elif choice == 4:
            while 1:
                dnsmap_inp = prompt("DNS MAP (URL) >> ")
                break
            dnsmap(dnsmap_inp)
            continue

        elif choice == 5:
            while 1:
                img_path = prompt("Metadata (PATH) >> ")
                break
            gps_analyzer(img_path)
            continue

        elif choice == 6:
            while 1:
                img = prompt("REVERSE IMAGE SEARCH (PATH) >> ")
                break
            reverseimagesearch(img)
            continue

        elif choice == 7:
            while 1:
                hp_inp = prompt("HONEYPOT (IP) >> ")
                break
            honeypot(hp_inp)
            continue

        elif choice == 8:
            while 1:
                mac = prompt("MAC ADDRESS LOOKUP (Eg:08:00:69:02:01:FC) >> ")
                break
            MacAddressLookup(mac)
            continue

        elif choice == 9:
            while 1:
                IPHeatmap()
                break
            continue

        elif choice == 10:
            while 1:
                IP = prompt("IPADDRESS (Eg:192.168.1.1) >> ")
                break
            torrent(IP)
            continue

        elif choice == 11:
            while 1:
                print("\n1.Facebook \n2.Twitter \n3.Instagram\n")
                username = input("Username >> ")
                choice = input("choice >> ")
                break
            user(choice,username)
            continue

        elif choice == 12:
            while 1:
                IP = prompt("IPADDRESS (Eg:192.168.1.1) >> ")
                break
            ip2Proxy(IP)
            continue

        elif choice == 13:
            while 1:
                web = prompt("MAIL ADDRESS (Eg:intercom.io) >> ")
                break
            maildb(web)
            continue

        elif choice == 99:
            while 1:
                break
            update()
            continue

        elif choice == 0:
            exit('\nBye, See ya again..')

        else:
            pass


# Handling ctrl+c
try:
    repl()
except KeyboardInterrupt:
    quit('\nBye, See ya again..')
