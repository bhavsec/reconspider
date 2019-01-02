<h1 align="center">
<a href="https://github.com/bhavsec/reconspider"><img src="http://reconspider.com/images/reconspider.png" alt="ReconSpider 		height="200" width="200""></a>
</h1>
<h4 align="center"> Most advanced Open Source Intelligence (OSINT) Framework </h4>
<p align="center">
<a href="https://github.com/bhavsec/reconspider/releases"><img src="https://img.shields.io/badge/release-1.0.5%20(beta)-blue.svg">
<a href="https://travis-ci.com/bhavsec/reconspider"><img src="https://api.travis-ci.com/bhavsec/reconspider.svg">
</p>

# ReconSpider

ReconSpider is most Advanced Open Source Intelligence (OSINT) Framework for scanning IP Address, Emails, Websites, Organizations and find out information from different sources.

ReconSpider can be used by Infosec Researchers, Penetration Testers, Bug Hunters and Cyber Crime Investigators to find deep information about their target.

ReconSpider aggregate all the raw data, visualize it on a dashboard and facilitate alerting and monitoring on the data.



# Why it's called ReconSpider ?

```ReconSpider```  =  ```Recon```  +  ```Spider```


<b>Recon</b> = Reconnaissance

Reconnaissance is a mission to obtain information by various detection methods, about the activities and resources of an enemy or potential enemy, or geographic characteristics of a particular area.


<b>Spider</b> = Web crawler

A Web crawler, sometimes called a spider or spiderbot and often shortened to crawler, is an Internet bot that systematically browses the World Wide Web, typically for the purpose of Web indexing (web spidering).



# Table Of Contents

1. [Version (beta)](https://github.com/bhavsec/reconspider#version-beta)
2. [Overview of the tool](https://github.com/bhavsec/reconspider#overview-of-the-tool)
3. [Mind Map (v1)](https://github.com/bhavsec/reconspider#mind-map-v1)
4. [License Information](https://github.com/bhavsec/reconspider#license-information)
5. [ReconSpider Banner](https://github.com/bhavsec/reconspider#reconspider-banner)
6. [Documentation](https://github.com/bhavsec/reconspider#documentation)
7. [Setting up the environment (Linux Operating System)](https://github.com/bhavsec/reconspider#setting-up-the-environment-linux-operating-system)
8. [Setting up the environment (Windows Operating System)](https://github.com/bhavsec/reconspider#setting-up-the-environment-windows-operating-system)
9. [Usage](https://github.com/bhavsec/reconspider#usage)
10. [Contact](https://github.com/bhavsec/reconspider#contact)
11. [Updates](https://github.com/bhavsec/reconspider#frequent--seamless-updates)


# Version (beta)

  	ReconSpider   :     1.0.5
  	Website       :     reconspider.com



# Overview of the tool:

* Performs OSINT scan on a IP Address, Emails, Websites, Organizations and find out information from different sources.
* Correlates and collaborate the results, show them in a consolidated manner. 
* Use specific script / launch automated OSINT for consolidated data.
* Currently available in only Command Line Interface (CLI).



# Mind Map (v1)

Check out our mind map to see visually organize information of this tool regarding api, services and techniques and more.
```
http://reconspider.com/mindmap.html
```



# License Information
```
ReconSpider and its documents are covered under GPL-3.0 (General Public License v3.0)
```



## ReconSpider Banner

```
__________                               _________       __     ___            
\______   \ ____   ____  ____   ____    /   _____/_____ |__| __| _/___________ 
 |       _// __ \_/ ___\/  _ \ /    \   \_____  \\____ \|  |/ __ |/ __ \_  __ \
 |    |   \  ___/\  \__(  <_> )   |  \  /        \  |_> >  / /_/ \  ___/|  | \/
 |____|_  /\___  >\___  >____/|___|  / /_______  /   __/|__\____ |\___  >__|   
        \/     \/     \/           \/          \/|__|           \/    \/       

                      developer: https://bhavkaran.com


usage: python reconspider.py

ENTER 0 - 7 TO SELECT OPTIONS

1. IP             Enumerate information from IP Address
2. URL            Gather information about given Website
3. WHOIS          Gather domain registration information
4. DNS MAP        Map DNS records associated with the target
5. PORT SCAN      Discover hosts and services on a network
6. NS LOOKUP      Obtain domain name or IP address mapping
7. HONEYPOT       Check if it's honeypot or a real control system

0.  EXIT          Exit from ReconSpider Framework
```



# Documentation

Installing and using ReconSpider is very easy. Installation process is very simple.

1. Downloading or cloning ReconSpider github repository.
2. Installing all dependencies.

Let's Begin !!



### Setting up the environment (Linux Operating System)

Step 1 - Cloning ReconSpider on your linux system.

In order to download ReconSpider simply clone the github repository. Below is the command which you can use in order to clone ReconSpider repository.
```
git clone https://github.com/bhavsec/reconspider.git
```


Step 2 - Installing all dependencies.

Once you clone, you will find directory name as **reconspider**. Just go to that directory and install using these commands:
```
cd reconspider
sudo python setup.py install
```



### Setting up the environment (Windows Operating System)

Step 1 - Downloading ReconSpider on your windows system.

In order to download ReconSpider from github repository simply copy and paste this URL in your favourite browser.
```
https://github.com/bhavsec/reconspider/archive/master.zip
```

Step 2 - Unzipping the file

Once you download, you will find zipped file name as **datasploit-master.zip**. Just right click on that zipped file and unzip the file using any software like [WinZip](https://www.winzip.com/), [WinRAR](https://www.win-rar.com).


Step 2 - Installing all dependencies.

After unzipping, go to that directory using Command Prompt and type the following command.
```
python setup.py install
```



# Usage 


ReconSpider is very handy tool and easy to use. All you have to do is just have to pass values to parameter. 
In order to start ReconSpider just type:
```
python reconspider.py
```

**1. IP**

This option gathers all the information of given IP Address from public resources.
```
ReconSpider >> 1
IP >> 8.8.8.8
```

**2. URL**

This option gathers all the information of given URL Address from public sources and give you in depth-information of IP address, country, city, organization, ISP, open ports and so more.
```
ReconSpider >> 2
URL >> vulnweb.com
```

**3. WHOIS**

This option allows you to search for domain name availability and WHOIS information including name, organisation, address, city, country, zipcode, registrar, name servers etc.
```
ReconSpider >> 3
WHOIS (URL) >> google.com
```

**4. DNS MAP**

This option allows you to map an organizations attack surface with a virtual DNS Map of the DNS records associated with the target organization.
```
ReconSpider >> 4
DNS MAP (URL) >> vulnweb.com
```

**5. PORT SCAN**

This option allows you to determine what hosts are available on the network, what services (application name and version) those hosts are offering, what operating systems (and OS versions) they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics.
```
ReconSpider >> 5
PORT SCAN (URL / IP) >> vulnweb.com
```

**6. NS LOOKUP**

This option allows you to obtain information about internet servers. It finds name server information for domains by querying the Domain Name System.
```
ReconSpider >> 6
NS LOOKUP (URL) >> google.com
```

**7. HONEYPOT**

This option allows you to identify honeypots! The probability that an IP is a honeypot is captured in a "Honeyscore" value that can range from 0.0 to 1.0
```
ReconSpider >> 7
HONEYPOT (IP) >> 1.1.1.1
```

**0. EXIT**

This option allows you to Exit from ReconSpider Framework.
```
ReconSpider >> 0
```
Output:
```
Bye, See ya again..
```



# Contact

Do you want to have a conversation in private? Hit me up on these social networks:

    Twitter:            @bhavsec
    Facebook:           fb.com/Mr.BhavKaran
    Instagram:          instagram.com/bhav_karan
    LinkedIn:           linkedin.com/in/bhav
    Website:            bhavkaran.com



# Frequent & Seamless Updates
ReconSpider is under heavy development and updates for fixing bugs. optimizing performance & new features are being rolled regularly.

Custom error handling is also not implemented, and all the focus is to create required functionality. 

If you would like to see features and issues that are being worked on, you can do that on [Development Progress](https://github.com/bhavsec/reconspider/projects/1) project board.
