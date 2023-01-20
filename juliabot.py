from re import search
import tweepy
import time

api_key = 'XXXXXXXXXXXXXXXXXXX'
api_secret_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
acess_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
acess_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acess_key, acess_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

JULIA = "julia"

def _main_():
    public_tweets = api.search_tweets(JULIA)
    for tweet in public_tweets:
        text = tweet.text
        user = tweet.user.name
        if JULIA in text and user:
            id = tweet.id
    api.retweet(id)

while True:
    _main_()
    time.sleep(3600)
