import nmap
import json

def DefaultPort(Xhost, Yport):
    print('')
    print("Starting port scan with range 22-443")
    nm = nmap.PortScanner()
    result = nm.scan(Xhost, '22-443')
    display(result)

def Customrange(Xhost, Yport):
        print('')
        port_range = input("Enter the range : ")
        print('')
        print("Starting port scan with range %s"%port_range)
        nm = nmap.PortScanner()
        result = nm.scan(Xhost, port_range)
        display(result)

def display(result):
    new = next(iter(result['scan'].values()))
    ip_add = new['addresses']
    print('')
    print("IP Address : %s" % ip_add['ipv4'])
    hosting = new['hostnames']
    hostname0 = hosting[0]
    hostname1 = hosting[1]
    print('')
    print("Hostname 1  : %s" % hostname0['name'])
    print("Hostname 2  : %s" % hostname1['name'])
    print('')
    print("Open Ports  : ")
    print('')
    ports = new['tcp']
    json_scan = json.dumps(ports)
    parsed = json.loads(json_scan)
    print(json.dumps(parsed, indent=4, sort_keys=True))
print('')
