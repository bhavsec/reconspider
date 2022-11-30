import requests
from bs4 import BeautifulSoup
import tweepy

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
    auth = tweepy.OAuthHandler("f0rCnr7Tln5EnIqiD6JcuMIJ8", "DmwOASEbukzltfyZx66KQGbguORJkEqpZdGMNvbiefJoIeYvWl")
    auth.set_access_token("884691164900737025-nTLY2Z4KVMX4IS294Ap43hPxmDZrXSW", "oDo8dV8RgPaJpa6ifYFgp5F0K7huAb1rIhhUSl2p2ewxA")
    api = tweepy.API(auth)
    screen_name = username
    user = api.get_user(screen_name)
    

    try:
       print("Full Name of the User is : " + user.screen_name)
    except Exception as e:
       print("User Name -->"+" Not Found" + str(e))
    print()

    try:
      ID = user.id_str
      print("The ID of the user is : " + ID)
    except Exception as e:
      print("User Id--> "+"Not Found" + str(e))
    print()
    
    for friend in api.friends(screen_name):
      print(friend.screen_name)

    description = api.blocks_ids(screen_name)
    print("This User is blocked by : " + str(description))



