from urllib.request import urlopen

def ClickJacking(host, port):

    if port == 80:
          port = 'http://'
    elif port == 443:
          port = 'https://'
    else:
         print("Could'nt fetch data for the given PORT")


    url = (port+host)

    data = urlopen(url)
    headers = data.info()

    if not "X-Frame-Options" in headers:
          print("Website is vulnerable to ClickJacking")

    else:
        print("Website is not Vulnerable to ClickJacking")
