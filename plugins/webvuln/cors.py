import requests


header1 = None
domain2 = None
header2 = None
domain3 = None
header3 = None


def Cors(host, port):
    if port == 80:
        port = 'http://'
    elif port == 443:
        port = 'https://'
    else:
        print("Could'nt fetch data for the given PORT")
        exit()
    print("1. CORS check in Default Host")
    print("2. CORS check in Host's Custom Endpoint")
    print('')
    choice = int(input('CORS >>'))
    print('')
    cookies = input("Paste the Cookies (If None,then hit enter) : ")
    global header1
    global domain2
    global header2
    global domain3
    global header3
    if cookies == '':

        header1 = {'Origin': 'http://evil.com'}

        domain2 = host + '.evil.com'

        header2 = {'Origin': port + domain2}

        domain3 = host + '%60cdl.evil.com'

        header3 = {'Origin': port + domain3}

        Choices(host, port, choice)
    else:

        header1 = {'Origin': 'http://evil.com', 'Cookie': cookies}

        domain2 = host + '.evil.com'

        header2 = {'Origin': port + domain2,'Cookie': cookies}

        domain3 = host + '%60cdl.evil.com'

        header3 = {'Origin': port + domain3,'Cookie': cookies}

        Choices(host, port, choice)


def Choices(host, port, choice):
    if choice == 2:
        endpoint = input("Enter the Custom Endpoint : ")
        host = endpoint
        WrongChoice(host, port)

    elif choice == 1:
        print("Checking Default Host ")
        url = (port + host)
        print("Testing with Payload %s" % header1)
        response = requests.get(url, headers=header1)
        if 'evil.com' in response.headers:
            print("Vulnerable to Cross Origin Resource Sharing")
        else:
            print("Not Vulnerable to Cross Origin Resource Sharing")
        print('')

        print("Testing with Payload %s" % header2)
        response = requests.get(url, headers=header2)

        if domain2 in response.headers:
            print("Vulnerable to Cross Origin Resource Sharing")
        else:
            print("Not Vulnerable to Cross Origin Resource Sharing")
        print('')

        print("Testing with Payload %s" % header3)
        response = requests.get(url, headers=header3)
        if domain2 in response.headers:
            print("Vulnerable to Cross Origin Resource Sharing")
        else:
            print("Not Vulnerable to Cross Origin Resource Sharing")
        print('')
    else:
        print("Wrong Choice")
        print("Checking Default Host")
        WrongChoice(host, port)

def WrongChoice(host, port):
    url = (port + host)
    print("Testing with Payload %s" % header1)
    response = requests.get(url, headers=header1)
    if 'evil.com' in response.headers:
        print("Vulnerable to Cross Origin Resource Sharing")
    else:
        print("Not Vulnerable to Cross Origin Resource Sharing")
    print('')

    print("Testing with Payload %s" % header2)
    response = requests.get(url, headers=header2)

    if domain2 in response.headers:
        print("Vulnerable to Cross Origin Resource Sharing")
    else:
        print("Not Vulnerable to Cross Origin Resource Sharing")
    print('')

    print("Testing with Payload %s" % header3)
    response = requests.get(url, headers=header3)
    if domain2 in response.headers:
        print("Vulnerable to Cross Origin Resource Sharing")
    else:
        print("Not Vulnerable to Cross Origin Resource Sharing")
    print('')
