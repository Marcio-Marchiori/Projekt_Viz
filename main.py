import pandas as pd
import sqlalchemy as db
from dotenv import load_dotenv
import os
import tweepy
import psycopg2
from multiprocessing import Pool, cpu_count
#pool = Pool(processes=cpu_count())

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN =  os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET =  os.getenv("ACCESS_TOKEN_SECRET")
db_server = os.getenv("db_server")
user = os.getenv("user")
password = os.getenv("password")
ip = os.getenv("ip")
db_name = os.getenv("db_name")

auth = tweepy.AppAuthHandler(API_KEY, API_SECRET_KEY)

x=[]
#auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
query

def magic_8_b(to_be_queried)
    try:
        for tweet in tweepy.Cursor(api.search, q=to_be_queried, tweet_mode="extended").items(1000):
            x.append(tweet)

    except:
        print('shits fucked mate')
    
    finally:
        conn = psycopg2.connect(f"host={ip}  dbname={db_name} user={user} password={password}")
        cur = conn.cursor()
        for i in range(len(x)):    
            cur.execute("INSERT INTO tweets_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (x[i]._json['created_at'],x[i]._json['id'],x[i]._json['full_text'],x[i]._json['user']['followers_count'],x[i]._json['user']['friends_count'],x[i]._json['user']['location'],x[i]._json['user']['created_at'],to_be_queried))
        conn.commit()   