from datetime import datetime
import time
import re
import tweepy


api_key = 'XXXXXXXXXXXXXXXXXXX'
api_secret_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
acess_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
acess_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
bearer_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acess_key, acess_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

client = tweepy.Client(bearer_token)
client = tweepy.Client
data = api.rate_limit_status()


def _main_():
    for tweet in tweepy.Cursor(api.search_tweets, q="Júlia OR júlia OR julia OR Julia", lang="pt", result_type="recent").items(100):
        try:
            if re.search('Júlia|júlia|julia|Julia', tweet.text):
                api.retweet(tweet.id)
        except Exception as e:
            print(e)
            print("Erro ao tentar retweetar")


while True:
    _main_()
    print('Pausando busca por 30 minutos')
    print('Hora que foi pausado: ' + datetime.now().strftime('%d/%m/%Y %H:%M'))
    time.sleep(1800)
