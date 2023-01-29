from datetime import datetime
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
    for tweet in api.search_tweets(q=JULIA, lang="pt", result_type="recent", count=100):
        try:
             if JULIA in tweet.text:
                tweet.retweet()
        except Exception as e:
            print(e)
            print("Este tweet já foi retweetado")

while True:
    _main_()
    print('Pausando busca por 30 minutos')
    print('Hora que foi pausado: ' + datetime.now().strftime('%d/%m/%Y %H:%M')) 
    time.sleep(1800)
