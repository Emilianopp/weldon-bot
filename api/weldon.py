import tweepy 
import pandas as pd 
from bs4 import BeautifulSoup
import requests
from datetime import datetime
class api():

    def __init__(self):

        self.access='QyXwPCcDSW0cAyvfMKXi6XwrB'
        self.access_secret='UCHAfdf1NRuua3gpsBmZb631yGUbqkkPBptHjDm0Eryxw55gL2'
        self.access_token = '705069617295790080-pozC0WzNnYW0CTJbOuCOfJ3O3cr6Maj'
        self.access_token_secret = '19frJEBqOSFR05QGkfJWtznOuj3tqRh38zpVuDk92Jjr4'


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
            api.update_status(f"Current occupants {traffic}\n time:{current_time}")

                