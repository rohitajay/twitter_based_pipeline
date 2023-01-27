import time

import tweepy
from config import *


client = tweepy.Client(bearer_token, API_KEY, API_SECRET ,access_token=access_token,access_token_secret=access_token_secret)

auth = tweepy.OAuthHandler(API_KEY, API_SECRET, access_token, access_token_secret)

api = tweepy.API(auth)

search_terms = ["python", "programming", "coding"]

class MyStream(tweepy.StreamingClient):

    def on_connect(self):
        print("connected")

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            print(tweet.text)

            time.sleep(0.2)


stream = MyStream(bearer_token=bearer_token)

for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields= ["referenced_tweets"])