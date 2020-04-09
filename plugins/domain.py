import socket
from .webosint.cmsdetect import CMSdetect
from .webosint.nslookup import nsLookup
from .webosint.portscan import DefaultPort,Customrange
from .webosint.reverseip import ReverseIP
from .webosint.subdomain import SubDomain
from .webvuln.bruteforce import ssh
from .webvuln.clickjacking import ClickJacking
from .webvuln.cors import Cors
from .webvuln.hostheader import HostHeader
from .webosint.header import header
from .webosint.crawler import crawler
from .webosint.who.whoami import whoami
from .portscan import PortScan

# Checking whether the target host is alive or dead
def CheckTarget(host,port):
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, port))

    if  result == 0:
        return True
    else:
        return False

# Main Method
def domain(host,port):

    if CheckTarget(host,port)==True:
        print("\nTarget Alive \n")
        Menu(host,port)
    else:
        print("The Host is Unreachable \n")
        exit()


NmapFunctions = {
    1: DefaultPort,
    2: Customrange,
}


def nmaprec(host,port):
    try:
        Choice = 1
        while True:
            print("1. Scan Default Ports (22-443)")
            print("2. Enter Custom Range")
            print("3. Back to Main Menu")
            print('')
            Choice = int(input(">> "))
            if (Choice >= 0) and (Choice < 3):
                NmapFunctions[Choice](host, port)
            elif Choice == 3:
                Menu(host,port)
            else:
                print("Please choose an Appropriate option")
    except AttributeError:
        PortScan(host)


BruteFunctions = {1: ssh}

def BruteForce(host, port):
    print("\nBrute Forcing SSH")
    BruteFunctions[1](host,port)


MainFunctions = {
 1: ReverseIP,
 2: SubDomain,
 3: nsLookup,
 4: CMSdetect,
 5: nmaprec,
 6: BruteForce,
 7: ClickJacking,
 8: Cors,
 9: HostHeader,
 10:header,
 11:crawler,
 12:whoami
}

def Menu(host,port):
    Selection = 1
    while True:
        print('')
        print("1."+" ReverseIP")
        print("2."+" SubDomain")
        print("3."+" nsLookup")
        print("4."+" CMSDetect")
        print("5."+" PortScan")
        print("6."+" Bruteforce")
        print("7."+" ClickJacking")
        print("8."+" CORS")
        print("9."+" Host Header Injection")
        print("10."+" Header")
        print("11."+" Crawler")
        print("12."+" Whoami")
        print("99."+" Exit")
        print('')
        Selection = int(input("Domain >> "))
        if (Selection >= 0) and (Selection <=12):
            MainFunctions[Selection](host, port)
        elif Selection == 99:
            return
        else:
            print("Error: Please choose an Appropriate option")
        print('')
