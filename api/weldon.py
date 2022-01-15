
import pandas as pd 
import tweepy 
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import yaml
class api():

    def __init__(self):
        with open('./secrets/auth.yaml', 'r') as f:
            p = yaml.safe_load(f)
        self.access=p['access']
        self.access_secret=p['access_secret']
        self.access_token = p['access_token']
        self.access_token_secret = p['access_token_secret']


    def get_traffic(self):
        url = requests.get('https://www.lib.uwo.ca/taps/tapper?lib=wel').text
        soup = BeautifulSoup(url, "html.parser")
        result = soup.find("div", {"id": "current"}).text.replace("Occupants","")
        return result

    def OAuth(self):
        try:
            auth = tweepy.OAuthHandler(self.access,self.access_secret)
            auth.set_access_token(self.access_token,self.access_token_secret)
            return auth
        except Exception as e:
            print(e)


    def tweet_traffic(self,traffic):
        if traffic != None:
            oauth = self.OAuth()
            api = tweepy.API(oauth)
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            api.update_status(f"Weldon current occupants {traffic} \n time:{current_time}")

                