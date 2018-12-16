# ReconSpider

ReconSpider is a powerful tool to perform Open Source Intelligence (OSINT) scan on email/domain/ip_address/organization. ReconSpider aggregate all the raw data, visualize it on a dashboard and facilitate alerting and monitoring on the data. ReconSpider can be used by Infosec Researchers, Penetration Testers, Bug Hunters and Cyber Crime Investigators to find deep information about their target.



# Version (beta)

	File Name     :     README
	Developer     :     @bhavsec
	Version       :     0.0.1
	Website       :     reconspider.com



# Overview of the tool:

* Performs OSINT on a Domain / Email / IP Address and find out information from different sources.
* Correlates and collaborate the results, show them in a consolidated manner. 
* Use specific script / launch automated OSINT for consolidated data.
* Currently Available in only Console.



# Licenses information

ReconSpider and its documents are covered with GPL-3.0 (General Public License v3.0)



## Using ReconSpider

```
__________                               _________       __     ___            
\______   \ ____   ____  ____   ____    /   _____/_____ |__| __| _/___________ 
 |       _// __ \_/ ___\/  _ \ /    \   \_____  \\____ \|  |/ __ |/ __ \_  __ \
 |    |   \  ___/\  \__(  <_> )   |  \  /        \  |_> >  / /_/ \  ___/|  | \/
 |____|_  /\___  >\___  >____/|___|  / /_______  /   __/|__\____ |\___  >__|   
        \/     \/     \/           \/          \/|__|           \/    \/       

                      developer: https://bhavkaran.com


usage: reconspider.py [OPTIONS]

OPTIONS:

  --ip                  Enumerate information from IP Address.
  --url                 Enumerate information from given Website.
  --whois               Gather domain registration information.
  --email               Gather information from email address.
  --domain              Gather detail of website or organization.
  --help                Show this help message and exit.
```



# Required setup

* Python 2.7            Download latest version from here: [python.org](https://www.python.org/downloads/)
* Use install.py        For installing all dependencies and libraries



# Documentation

Installing and using ReconSpider is very easy. Installation process is very simple.

1. Downloading or cloning ReconSpider github repository.
2. Downloading and installing all dependencies.
3. Generating and adding API Keys in config file

Let's Begin !!



### Setting up the environment (Linux Operating System)

Step 1 - cloning ReconSpider on your linux system.

In order to download ReconSpider simply clone the github repository. Below is the command which you can use in order to clone ReconSpider repository.
```
git clone https://github.com/bhavsec/reconspider.git
```


Step 2 - Installing all dependencies.

Once you clone, you will find directory name as **reconspider**. Just go to that directory and install dependencies. If you are using ReconSpider on windows then run install_linux.py file and if you are using linux then run install_linux.py
```
python install.py
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
python install.py
```

### Generating and adding API Keys

We need some API Keys before using this tool. Following are the API's which we are using in this tool for a time being.

1. Shodan API
2. Clearbit API
3. Fullcontact API



**Shodan API**

Register yourself at [Shodan](https://account.shodan.io/register) and activate your account.
Once you login, [Click here](https://account.shodan.io/) to get API Key.
Copy that key and paste inside config.py file in modules directory.

(free account: basic search capabilities. Premium account with full access is a one-time payment of $50 and pretty worth it)



**Clearbit API**

Register yourself at [Clearbit](https://dashboard.clearbit.com/signup) and activate your account.
Once you login, [Click here](https://dashboard.clearbit.com/api) to get API Key.
Copy secret API key and paste inside config.py file in modules directory.



**FullContact API**

Register yourself at [Full Contact](https://www.fullcontact.com/developer/)  and activate your account.
Once you login, [Click here](https://dashboard.fullcontact.com/) to get API Key.
Click on [+ Generate New API Key] button and copy that key and paste it inside config.py file in modules directory.

(free account: 500 Person and Company matches per month, and 60 queries per minute)



# Developer

    Name                BhavKaran Singh Chahal
    Twitter:            @bhavsec
    Facebook:           fb.com/Mr.BhavKaran
    LinkedIn:           linkedin.com/in/bhav
    Website:            bhavkaran.com



# Usage 


ReconSpy is very handy tool and easy to use. All you have to do is just have to pass values to parameter. 
In order to start ReconSpider just type:
```
python reconspider.py
```

**--ip**

This feature gathers all the information of given IP Address from public sources.
```
python reconspider.py  --ip 8.8.8.8
```

**--url**

This feature gathers all the information of given URL Address from public sources and give you in depth-information of IP address, country, city, organization, ISP, open ports and so more.
``` 
python reconspider.py  --url google.com 
```

**--whois**

This feature allows you to search for domain name availability and WHOIS information including name, organisation, address, city, country, zipcode, registrar, name servers etc.
```
python reconspider.py  --whois google.com
```

**--email**

This feature gathers information about given email address from various public sources including personal details, location, employment details, social accounts and so more.

```
python reconspider.py  --email bill.gates@microsoft.com
```

**--domain**

This feature give you in depth-information about particular domain including locations, description, emails, employees and so more.

```
python reconspider.py  --domain google.com
```



# Note
```
Currently project is in developement phase and lot of work is going on. Custom error handling is also not implemented, and all the focus is to create required functionality. 
```
