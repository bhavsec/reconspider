import os
import platform

if (platform.system() != "Windows"):
    os.system('apt-get install python-pip')
    os.system('pip install clearbit')
    os.system('pip install shodan')
    os.system('pip install fullcontact.py')
    os.system('pip install steganography')
    os.system('pip install requests')
    os.system('pip install sslscan')
    os.system('pip install pythonwhois')
else:
    os.system('C:\Python27\Scripts\pip install clearbit')
    os.system('C:\Python27\Scripts\pip install shodan')
    os.system('C:\Python27\Scripts\pip install fullcontact.py')
    os.system('C:\Python27\Scripts\pip install steganography')
    os.system('C:\Python27\Scripts\pip install requests')
    os.system('C:\rPython27\Scripts\pip install sslscan')
