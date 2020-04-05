from setuptools import setup
import os

fout = open("core/config.py", "w")
fout.write("shodan_api = " + '"' + "C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by" + '"' + "\n")
fout.close()

setup(
    name="ReconSpider",
    version="1.0.5",
    description="Most Advanced OSINT Framework",
    url="https://github.com/bhavsec/reconspider/",
    author="BhavKaran (@bhavsec)",
    author_email="contact@bhavkaran.com",
    license="GPL-3.0",
    install_requires=["shodan", "requests", "prompt_toolkit","wget","beautifulsoup4","click","urllib3","IP2proxy","wget","paramiko","h8mail","nmap","pythonping","whois","gmplot","pillow"],
    console=["reconspider.py"],
)

import wget

#Database
url="https://www.ip2location.com/download?token=hg5uYe2Jvri4R7P1j8b71Pk8dnvIU2M6A9jz2tvcVtGx8ZK2UPQgzr6Hk3cV68oH&file=PX8LITEBIN"
print('\nDownloading IP2PROXY-IP-PROXYTYPE-COUNTRY-REGION-CITY-ISP-DOMAIN-USAGETYPE-ASN-LASTSEEN.BIN...')
filepath=os.getcwd()+"/plugins/"
wget.download(url,out=filepath)
print('\nDownload Finished')

import zipfile
print('\nExtracting Files')
with zipfile.ZipFile(filepath+"IP2PROXY-LITE-PX8.BIN.ZIP","r") as zip_ref:
    zip_ref.extract("IP2PROXY-LITE-PX8.BIN",filepath)

print("\nInstallation Successfull")
