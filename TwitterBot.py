import tweepy
from time import sleep
from DataManager import DataManager
consumer_key='cs7oDprWACHtinTZm7RvfPbYe'
consumer_secret='SzS1ml4oh2jNK5iT146R26vObVO4rPJqZM7mp5K4RNvpXx1mw8'
access_token='792172843324899329-8OE695NCOfJ7toMqa2BEBTRvFcRXAOt'
access_token_secret='JLG992xN4DpbGwNAMbHho4ZmqTw3S2uFUSPmuntm8E6Sw'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
auth.secure = True
api = tweepy.API(auth)
myBot = api.get_user(screen_name = '@DidTheFoxesWin')
myList = api.get_list("@"+myBot.screen_name,slug='sorry-for-adding-you')
myData = DataManager("DataFile.txt")
listData = DataManager("listData.txt")
count403 = 0
print("Running bot: @" + myBot.screen_name + "\n Using list: " + myList.name + " \n Members count:" + str(myList.member_count) + " Subs count: " + str(myList.subscriber_count))

for tweet in tweepy.Cursor(api.search,q='#Marist').items():
    try:
        if (tweet.user.id == myBot.id) or (myData.is_stored_b(str(tweet.id))):
            continue
        myData.add_data(str(tweet.id))
        print("\n\nFound tweet by: @" + tweet.user.screen_name)
        if(tweet.retweeted == False) or (tweet.favorited == False):
            tweet.retweet()
            tweet.favorite()
            print("Retweeted and favorited the tweet")
        if not listData.is_stored_b(str(tweet.user.id)):
            #api.add_list_member(screen_name = tweet.user.screen_name, owner_screen_name = myBot.screen_name, list_id = myList.id)
            listData.add_data(str(tweet.user.id))
            print("Added the user to the list")
        if tweet.user.following == False:
            tweet.user.follow()
            print("Followed the user")
        count403 = 0
    except tweepy.TweepError as e:
        print(e.reason)
        if "403" in e.reason:
            if count403 > 15:
                print("There are too many 403 errors. Pausing for 30 mins")
                sleep(1800)
            else:
                count403 += 1
                print("Another 403 error. Total: " + str(count403))
                sleep(1)
        else:
           sleep(10) 
        
        continue
    except StopIteration:
        break
