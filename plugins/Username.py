import requests
from bs4 import BeautifulSoup

out=[]

def user(choice,username):
    if choice == '1':
        pass
    elif choice == '2':
        ScrapTweets(username)
        return()
    elif choice == '3':
        Instagram(username)
        return()
    else:
        exit()

    search_string = "https://en-gb.facebook.com/" + username

    #response is stored after request is made
    response = requests.get(search_string)

    #Response is stored and parsed to implement beautifulsoup
    soup = BeautifulSoup(response.text, 'html.parser')

    #List that will store the data that is to be fetched

    ###Finding Name of the user
    #Min div element is found which contains all the information
    main_div = soup.div.find(id="globalContainer")

    #finding name of the user
    def find_name():
        name = main_div.find(id="fb-timeline-cover-name").get_text()
        print("\n"+"Name:"+name)

    ###Finding About the user details
    #finding work details of the user
    def find_eduwork_details():
        try:
            education = soup.find(id="pagelet_eduwork")
            apple=education.find(attrs={"class":"_4qm1"})
            if (apple.get_text() != " "):
                for category in education.find_all(attrs={"class":"_4qm1"}):
                    print(category.find('span').get_text() + " : ")
                    for company in category.find_all(attrs={"class":"_2tdc"}):
                        if (company.get_text() != " "):
                            print(company.get_text())
                        else:
                            continue
            else:
                print("No work details found")
        except Exception as e:
            print(str(e))
        print()

    #finding home details of the user
    def find_home_details():
        if(soup.find(id="pagelet_hometown") !=" "):
                home = soup.find(id="pagelet_hometown")
                for category in home.find_all(attrs={"class":"_4qm1"}):
                    print(category.find('span').get_text() + " : ")
                    for company in category.find_all(attrs={"class":"_42ef"}):
                        if (company.get_text() != " "):
                            print(company.get_text())
                        else:
                            continue
        else:
            print("No Home details found")

    #finding contact details of the user


    ###Logic for finding the status of the response
    if ("200" in str(response)):
        find_name()
        find_eduwork_details()
        find_home_details()

    elif ("404" in str(response)):
        print("Error: Profile not found")
    else:
        print("Error: some other response")
    return()

def Instagram(username):

    r = requests.get("https://www.instagram.com/"+ username +"/?__a=1")
    if r.status_code == 200:
        res = r.json()['graphql']['user']
        print("\nUsername: " + res['username'])
        print("Full Name: "+res['full_name'])
        try:
            print("Business Category: "+res['edge_follow']['business_category_name'])
        except Exception as e:
            print("Account :"+" Private" + str(e))
        finally:
            print("Biograph: " + res['biography'])
            print("URL: "+ str(res['external_url']))
            print("Followers: "+str(res['edge_followed_by']['count']))
            print("Following: "+str(res['edge_follow']['count']))
            print("Profile Picture HD: " + res['profile_pic_url_hd'])
    elif r.status_code == 404:
        print("Error: Profile Not Found")
    else:
        print("Error: Something Went Wrong")

def ScrapTweets(username):

    link = "https://twitter.com/" + username

    page_html=requests.get(link).content
    soup = BeautifulSoup(page_html, 'html.parser')

    try:
        full_name = soup.find('a', attrs={"class": "ProfileHeaderCard-nameLink u-textInheritColor js-nav"})
        print("User Name --> " + full_name.text)
    except Exception as e:
        print("User Name -->"+" Not Found" + str(e))
    print()

    try:
        user_id = soup.find('b', attrs={"class": "u-linkComplex-target"})
        print("User Id --> " + user_id.text)
    except Exception as e:
        print("User Id --> "+"Not Found" + str(e))
    print()

    try:
        decription = soup.find('p', attrs={"class": "ProfileHeaderCard-bio u-dir"})
        print("Description --> " + decription.text)
    except Exception as e:
        print("Decription not provided by the user" + str(e))
    print()

    try:
        user_location = soup.find('span', attrs={"class": "ProfileHeaderCard-locationText u-dir"})
        print("Location -->  " + user_location.text.strip())
    except Exception as e:
        print("Location not provided by the user" + str(e))
    print()

    try:
        connectivity = soup.find('span', attrs={"class": "ProfileHeaderCard-urlText u-dir"})
        tittle = connectivity.a["title"]
        print("Link provided by the user --> " + tittle)
    except Exception as e:
        print("No contact link is provided by the user" + str(e))
    print()

    try:
        join_date = soup.find('span', attrs={"class": "ProfileHeaderCard-joinDateText js-tooltip u-dir"})
        print("The user joined twitter on --> " + join_date.text)
    except Exception as e:
        print("The joined date is not provided by the user" + str(e))
    print()

    try:
        birth = soup.find('span', attrs={"class": "ProfileHeaderCard-birthdateText u-dir"})
        birth_date = birth.span.text
        print("Date of Birth:"+birth_date.strip())
    except Exception as e:
        print("Birth Date not provided by the user" + str(e))
    print()

    try:
        span_box = soup.findAll('span', attrs={"class": "ProfileNav-value"})
        print("Total tweets --> " + span_box[0].text)
    except Exception as e:
        print("Total Tweets --> Zero" + str(e))
    print()

    try:
        print("Following --> " +span_box[1].text)
    except Exception as e:
        print("Following --> Zero" + str(e))
    print()

    try:
        print("Followers --> " + span_box[2].text)
    except Exception as e:
        print("Followers --> Zero" + str(e))
    print()

    try:
        print("Likes send by him --> " + span_box[3].text)
    except Exception as e:
        print("Likes send by him --> Zero" + str(e))
    print()

    try:
        if span_box[4].text != "More ":
            print("No. of parties he is Subscribed to --> " + span_box[4].text)
        else:
            print("No. of parties he is Subscribed to --> Zero")
    except Exception as e:
        print("No. of parties he is Subscribed to --> Zero" + + str(e))
    print()

    #spana = soup.findAll('span', attrs={"class": "ProfileNav-value"})

    print("Tweets by "+ username + " are --> ")
    # TweetTextSize TweetTextSize--normal js-tweet-text tweet-text
    for tweets in soup.findAll('p', attrs={"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}):
        print(tweets.text)
        print()
