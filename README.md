<h1 align="center">
<a href="https://github.com/bhavsec/reconspider"><img src="http://bhavkaran.com/reconspider/reconspider.png" alt="ReconSpider" height="200" width="200"></a>
</h1>

<h4 align="center"> Most Advanced Open Source Intelligence (OSINT) Framework </h4>

<p align="center">
<a href="https://github.com/bhavsec/reconspider/releases"><img src="https://img.shields.io/github/v/release/bhavsec/reconspider">
<a href="https://travis-ci.com/bhavsec/reconspider"><img src="https://api.travis-ci.com/bhavsec/reconspider.svg"></a>
<a class="badge-align" href="https://www.codacy.com/app/bhavsec/reconspider?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=bhavsec/reconspider&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/107277982d6a4f2b9c55bba0d66d8051"/></a>

</p>

# ReconSpider

ReconSpider is most Advanced Open Source Intelligence (OSINT) Framework for scanning IP Address, Emails, Websites, Organizations and find out information from different sources.

ReconSpider can be used by Infosec Researchers, Penetration Testers, Bug Hunters and Cyber Crime Investigators to find deep information about their target.

ReconSpider aggregate all the raw data, visualize it on a dashboard and facilitate alerting and monitoring on the data.

Recon Spider also combines the capabilities of [Wave](https://github.com/adithyan-ak/WAVE),[Photon](https://github.com/s0md3v/Photon) and [Recon Dog](https://github.com/s0md3v/ReconDog) to do a comprehensive enumeration of attack surface.

# Why it's called ReconSpider ?

```ReconSpider```  =  ```Recon```  +  ```Spider```


<b>Recon = Reconnaissance</b>

Reconnaissance is a mission to obtain information by various detection methods, about the activities and resources of an enemy or potential enemy, or geographic characteristics of a particular area.


<b>Spider = Web crawler</b>

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
11. [Wiki & How-to Guide](https://github.com/bhavsec/reconspider#reconspider-full-wiki-and-how-to-guide)
12. [Updates](https://github.com/bhavsec/reconspider#frequent--seamless-updates)


# Version (beta)

  	ReconSpider   :     1.0.6


# Overview of the tool:

* Performs OSINT scan on a IP Address, Emails, Websites, Organizations and find out information from different sources.
* Correlates and collaborate the results, show them in a consolidated manner.
* Use specific script / launch automated OSINT for consolidated data.
* Currently available in only Command Line Interface (CLI).



# Mind Map (v1)

Check out our mind map to see visually organize information of this tool regarding api, services and techniques and more.
```
http://bhavkaran.com/reconspider/mindmap.html
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


ENTER 0 - 13 TO SELECT OPTIONS

1.  IP                           Enumerate  information  from  IP Address
2.  DOMAIN                       Gather  information  about  given DOMAIN
3.  PHONENUMBER                  Gather  information  about   Phonenumber
4.  DNS MAP                      Map DNS  records associated  with target
5.  METADATA                     Extract all metadata of  the  given file
6.  REVERSE IMAGE SEARCH         Obtain domain name or IP address mapping
7.  HONEYPOT                     Check if it's honeypot or a real  system
8.  MAC ADDRESS LOOKUP           Obtain information about give Macaddress
9.  IPHEATMAP                    Draw  out  heatmap  of  locations  of IP
10. TORRENT                      Gather torrent download  history  of  IP
11. USERNAME                     Extract Account info. from social  media
12. IP2PROXY                     Check whether  IP  uses  any VPN / PROXY
13. MAIL BREACH                  Checks given domain  has  breached  Mail
99. UPDATE                       Update ReconSpider to its latest version

0. EXIT                         Exit from  ReconSpider  to your terminal
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

Step 2 - Make sure python3 and python3-pip is installed on your system.

You can also perform a check by typing this command in your terminal.

```
sudo apt install python3 python3-pip
```

Step 3 - Installing all dependencies.

Once you clone and check python installation, you will find directory name as **reconspider**. Just go to that directory and install using these commands:
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

Step 3 - Database

**IP2Proxy Database**
```
https://lite.ip2location.com/database/px8-ip-proxytype-country-region-city-isp-domain-usagetype-asn-lastseen
```
Download database, extract it and move to reconspider/plugins/ directory.


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

**2. DOMAIN**

This option gathers all the information of given URL Address and check for vulneribility.
```
Reconspider >> 2
HOST (URL / IP) >> vulnweb.com
PORT >> 443
```

**3. PHONENUMBER**

This option allows you to gather information of given phonenumber.
```
Reconspider >> 3
PHONE NUMBER (919485247632) >>
```

**4. DNS MAP**

This option allows you to map an organizations attack surface with a virtual DNS Map of the DNS records associated with the target organization.
```
ReconSpider >> 4
DNS MAP (URL) >> vulnweb.com
```

**5. METADATA**

This option allows you to extract all metadat of the file.
```
Reconspider >> 5
Metadata (PATH) >> /root/Downloads/images.jpeg
```

**6. REVERSE IMAGE SEARCH**

This option allows you to obtain information and similar image that are available in internet.
```
Reconspider >> 6
REVERSE IMAGE SEARCH (PATH) >> /root/Downloads/images.jpeg
Open Search Result in web broser? (Y/N) : y
```

**7. HONEYPOT**

This option allows you to identify honeypots! The probability that an IP is a honeypot is captured in a "Honeyscore" value that can range from 0.0 to 1.0
```
ReconSpider >> 7
HONEYPOT (IP) >> 1.1.1.1
```

**8. MAC ADDRESS LOOKUP**

This option allows you to identify Mac address details who is manufacturer, address, country, etc.

```
Reconspider >> 8
MAC ADDRESS LOOKUP (Eg:08:00:69:02:01:FC) >>
```

**9. IPHEATMAP**

This option provided you heatmap of the provided ip or single ip, if connect all the provided ip location with accurate Coordinator.
```
Reconspider >> 9

    1) Trace single IP
    2) Trace multiple IPs
OPTIONS >>
```

**10. TORRENT**

This option allows you to gathers history of Torrent download history.
```
Reconspider >> 10
IPADDRESS (Eg:192.168.1.1) >>
```

**11. USERNAME**

This option allows you to gathers account information of the provided username from social media like Instagram, Twitter, Facebook.
```
Reconspider >> 11

1.Facebook
2.Twitter
3.Instagram

Username >>
```

**12. IP2PROXY**

This option allows you to identify whether IP address uses any kind of VPN / Proxy to hide his identify.
```
Reconspider >> 12
IPADDRESS (Eg:192.168.1.1) >>
```

**13. MAIL BREACH**

This option allows you to identify all breached mail ID from given domain.
```
Reconspider >> 13
DOMAIN (Eg:intercom.io) >>
```

**99. UPDATE**

This option allows you to check for updates. If a newer version will available, ReconSpider will download and merge the updates into the current directory without overwriting other files.
```
ReconSpider >> 99
Checking for updates..
```

**0. EXIT**

This option allows you to exit from ReconSpider Framework to your current Operating System's terminal.
```
ReconSpider >> 0
Bye, See ya again..
```



# Contact Developer

Do you want to have a conversation in private?

    Twitter:            @bhavsec
    Facebook:           fb.com/bhavsec
    Instagram:          instagram.com/bhavsec
    LinkedIn:           linkedin.com/in/bhavsec
    Email:              contact@bhavkaran.com
    Website:            bhavkaran.com



# ReconSpider Full Wiki and How-to Guide

Please go through the [ReconSpider Wiki Guide](https://github.com/bhavsec/reconspider/wiki) for a detailed explanation of each and every option and feature.


# Frequent & Seamless Updates
ReconSpider is under heavy development and updates for fixing bugs. optimizing performance & new features are being rolled regularly. Custom error handling is also not implemented, and all the focus is to create required functionality.

If you would like to see features and issues that are being worked on, you can do that on [Development Progress](https://github.com/bhavsec/reconspider/projects/1) project board.



# Special Thanks

* [Adithyan AK](https://github.com/adithyan-ak)
* [S0md3v](https://github.com/s0md3v/)
* [Parshant](mailto:parshant.dhall@gmail.com)

