from api.weldon import api
import time
import csv
from datetime import datetime



def looper():
        now = datetime.datetime.now()
        end = now.replace(hour=23, minute=0, second=0, microsecond=0)
        caller = api()
        while 1: 
            traffic = caller.get_traffic()
            caller.tweet_traffic(traffic)
            with open('traffic.csv','a') as f:
                writer = csv.writer(f)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S-%d/%m/%Y")
                fields = [current_time,traffic]
                writer.writerow(fields)
                if current_time > end:
                    break; 
            time.sleep(1800)   






looper()

