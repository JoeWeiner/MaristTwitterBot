#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot written by Joseph Weiner for hackMarist 2016
#Inspired in part by LACUNY "Build a twitter bot day 2015"
#Credit for any directly copied code goes to the CUNY committe, however directly copied code is scarce as most things have been changed.

# This bot tweets a text file line by line
#Using a sleep method it rests for 30 seconds before completing the for loop

# This Twitter Bot takes from a generated text of the Marist Student Handbook and Code Of Conduct
#The aforementioned text file was generated by me for this specific project.
#It can be downloaded in the Git repository, however, I'm not sure what its use would be for a non-Marist Student


# do not edit
import requests
import tweepy
from time import sleep

#keys

CONSUMER_KEY = 'cs7oDprWACHtinTZm7RvfPbYe'
CONSUMER_SECRET = 'SzS1ml4oh2jNK5iT146R26vObVO4rPJqZM7mp5K4RNvpXx1mw8'

# Create a new Access Token
ACCESS_TOKEN = '792172843324899329-8OE695NCOfJ7toMqa2BEBTRvFcRXAOt'
ACCESS_SECRET = 'JLG992xN4DpbGwNAMbHho4ZmqTw3S2uFUSPmuntm8E6Sw'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
auth.secure = True
api = tweepy.API(auth)
print(str(api.get_user(screen_name = '@DidTheFoxesWin')))

# What the bot will tweet

filename = open('studentconduct.txt','r')
tweetText = filename.readlines()
filename.close()

for line in tweetText[0:3535]: #Will write all of the lines
    api.update_status(line)
    print (line)
    time.sleep(30) # Sleep for 30 seconds

print ("Complete!")

# To quit early: CTRL+C and wait a few seconds