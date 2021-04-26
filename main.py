import pandas as pd
import sqlalchemy as db
from dotenv import load_dotenv
import os
import tweepy
import psycopg2
import multiprocessing as mp
import logging
import time

def magic_8_b(to_be_queried):
    x=[]
    logging.basicConfig(filename='download.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    query_w = to_be_queried + ' -filter:retweets'
    try:
        auth = tweepy.AppAuthHandler(API_KEY, API_SECRET_KEY)
        api = tweepy.API(auth)
        for tweet in tweepy.Cursor(api.search, q=query_w, tweet_mode="extended",lang="en").items(1000):
            x.append(tweet)
        

    except:
        logging.warning('Failed ' + to_be_queried)

    else:
       logging.warning(to_be_queried + ' was successful.')
        
    finally:
        conn = psycopg2.connect(f"host={ip}  dbname={db_name} user={user} password={password}")
        cur = conn.cursor()
        for i in range(len(x)):    
            cur.execute("INSERT INTO tweets_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (x[i]._json['created_at'],x[i]._json['id'],x[i]._json['full_text'],x[i]._json['user']['followers_count'],x[i]._json['user']['friends_count'],x[i]._json['user']['location'],x[i]._json['user']['created_at'],to_be_queried))
        conn.commit()
        time.sleep(30)
  

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

if __name__ == "__main__":
    for qwerty in range(20):
        logging.basicConfig(filename='download.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        

        auth = tweepy.AppAuthHandler(API_KEY, API_SECRET_KEY)

        #auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        conn = psycopg2.connect(f"host={ip}  dbname={db_name} user={user} password={password}")
        cur = conn.cursor()
        query = 'SELECT name FROM people_to_query'
        cur.execute(query)
        x = cur.fetchall()
        conn.commit()
        zz = [i[0] for i in x]
        k = zz[:500]
        
        conn = psycopg2.connect(f"host={ip}  dbname={db_name} user={user} password={password}")
        cur = conn.cursor()
        query = 'select DISTINCT key_id from tweets_data'
        cur.execute(query)
        u = cur.fetchall()
        conn.commit()
        xx = [i[0] for i in u]
        v = list(set(k) - set(xx))
        
        with mp.Pool(4) as pool:
            download = pool.map(magic_8_b,v)
        time.sleep(300)
