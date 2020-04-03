import urllib.request

def ClickJacking(host, port):

    if port == 80:
          port = 'http://'
    elif port == 443:
          port = 'https://'
    else:
         print("Could'nt fetch data for the given PORT")


    url = (port+host)
    if url.lower().startswith('http'):
        data=urllib.request.urlretrieve(url)[1]
        headers=data.as_string()

    if not "X-Frame-Options" in headers:
          print("Website is vulnerable to ClickJacking")

    else:
        print("Website is not Vulnerable to ClickJacking")
