import requests

def ClickJacking(host, port):

    if port == 80:
          port = 'http://'
    elif port == 443:
          port = 'https://'
    else:
         print("Could'nt fetch data for the given PORT")


    url = (port+host)
    page=requests.get(url)
    headers=page.headers
    if not "X-Frame-Options" in headers:
          print("Website is vulnerable to ClickJacking")

    else:
        print("Website is not Vulnerable to ClickJacking")
