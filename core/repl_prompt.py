# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import socket

from plugins.censys import censys_ip
from plugins.dnsdump import dnsmap
from plugins.honeypot import honeypot
from plugins.nslookup import nslookup
from plugins.portscan import portscan
from plugins.shodan_io import shodan_host
from plugins.shodan_io import shodan_ip
from plugins.whois import whois
from core.updater import update
from prompt_toolkit import prompt


def repl():  # Read–eval–print loop
    while 1:
        user_input = prompt("\nReconspider >> ")
        if len(user_input) != 1:
            print("ENTER 1 - 7 TO SELECT OPTIONS")
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
                url_inp = prompt("URL >> ")
                break
            url = socket.gethostbyname(url_inp)  # URL to IP address conversion
            shodan_ip(url)
            continue

        elif choice == 3:
            while 1:
                whois_inp = prompt("WHOIS (URL) >> ")
                break
            whois(whois_inp)
            continue

        elif choice == 4:
            while 1:
                dnsmap_inp = prompt("DNS MAP (URL) >> ")
                break
            dnsmap(dnsmap_inp)
            continue

        elif choice == 5:
            while 1:
                port_inp = prompt("PORT SCAN (URL / IP) >> ")
                break
            portscan(port_inp)
            continue

        elif choice == 6:
            while 1:
                ns_inp = prompt("NS LOOKUP (URL) >> ")
                break
            nslookup(ns_inp)
            continue

        elif choice == 7:
            while 1:
                hp_inp = prompt("HONEYPOT (IP) >> ")
                break
            honeypot(hp_inp)
            continue

        elif choice == 8:
            while 1:
                break
            update()
            continue
        
        elif choice == 0:
            exit('\nBye, See ya again..')

# Handling ctrl+c
try:
    repl()
except KeyboardInterrupt:
    quit("")
