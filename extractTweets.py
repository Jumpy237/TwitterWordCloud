import codecs
import json
import ast
import re
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from termcolor import colored
from pymongo import MongoClient

keyword = input("enter keyword: ")  #keyword
collectionName = input("enter collection name: ") #collection you want to use

#My Twitter API KEY
ACCESS_TOKEN = '924789810169917440-1QtWmv3gV9BkeBHHK2W9v6K4zlkfPWP'
ACCESS_SECRET = 'wIogNzD3CBKaEbVHFAYFOed0FHmUpePlZyS6NCAmibAZg'
CONSUMER_KEY = 'k91yey7mL809b2MahmNCZhU8q'
CONSUMER_SECRET = 'DkLLjKQUUXEdVioiz5g1Hk6lUjdwIOln76TuonF7pwZb5jDjQX'


oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)  #twitter_stream object
tweets = twitter_stream.statuses.filter(track=keyword, language="en", tweet_mode="extended") #filtered twitter statuses

client = MongoClient()
db = client.myProject
collection = db[collectionName]

cnt = 0
for tweet in tweets:

    #print(tweet)

    tweet = ast.literal_eval(str(tweet)) #convert single quote to double quote
    tweet = json.dumps(ast.literal_eval(str(tweet)))
    tweet = json.loads(tweet) #convert to json
    if "text" in tweet:

        collection.insert_one(tweet) #insert into collection
        cnt += 1 #increment cnt by 1
        print(colored(str(cnt) + "/3000" + " tweets " ,"red"))
        print(tweet["text"])


    if cnt >= 3000:
        break

print("result : ",cnt,"tweets")
