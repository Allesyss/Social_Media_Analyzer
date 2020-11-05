#!/usr/bin/env python
# encoding: utf-8
# With reference to:  Author - Prateek Mehta


import tweepy #https://github.com/tweepy/tweepy
import json
import tkinter

#Twitter API credentials
consumer_key = "Enter the consumer_key"
consumer_secret = "Enter the consumer_secret"
access_key = "Enter the access_key"
access_secret = "Enter the access_secret"


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    print('Authorization successful')
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))
       
    #write tweet objects to JSON
    file = open('tweet_outcome.json', 'w')
    print "Writing tweet objects to JSON"
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
    print "Done"
    file.close()

def Get_Identity():
    consumer_key = entry_consumer_key.get()
    consumer_secret = entry_consumer_secret.get()
    access_key = entry_access_key.get()
    access_secret = entry_access_key.get()
    print(consumer_key)


if __name__ == '__main__':

    #creates an interface for the user to input the keys
    root = tkinter.Tk()
    label_consumer_key = tkinter.Label(root, text="consumer key:")
    label_consumer_key.place(relx=0.05, rely=0.2)
    entry_consumer_key = tkinter.Entry(root)
    entry_consumer_key.place(relx=0.3, rely=0.2, width=400)
    label_consumer_secret = tkinter.Label(root, text="consumer secret:")
    label_consumer_secret.place(relx=0.05, rely=0.4)
    entry_consumer_secret = tkinter.Entry(root)
    entry_consumer_secret.place(relx=0.3, rely=0.4, width=400)
    label_access_key = tkinter.Label(root, text="access key:")
    label_access_key.place(relx=0.05, rely=0.6)
    entry_access_key = tkinter.Entry(root)
    entry_access_key.place(relx=0.3, rely=0.6, width=400)
    label_access_secret = tkinter.Label(root, text="access secret:")
    label_access_secret.place(relx=0.05, rely=0.8)
    entry_access_secret = tkinter.Entry(root)
    entry_access_secret.place(relx=0.3, rely=0.8, width=400)
    button1 = tkinter.Button(root, text="confirm", command=Get_Identity)
    button1.place(relx=0.5, rely=0.95)
    root.mainloop()

    Get_Identity()

    #pass in the username of the account you want to download
    get_all_tweets("@ ... ")
