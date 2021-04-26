import pandas as pd
import sqlalchemy as db
from dotenv import load_dotenv
import os
import tweepy
import psycopg2
import multiprocessing as mp
import logging
import time
import re
from tqdm import tqdm


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

def regex_str(tweet_text):
    return [tweet_text[0], re.sub(r'@\S+|https?://\S+','',re.sub('[\n]','',tweet_text[1]))]

def regex_updt(str_to_up):
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
    conn = psycopg2.connect(f"host={ip}  dbname={db_name} user={user} password={password}")
    cur = conn.cursor()
    cur.execute("UPDATE tweets_data SET full_text = %s WHERE id = %s",(str_to_up[1],str_to_up[0]))
    conn.commit()


conn = psycopg2.connect(f"host={ip}  dbname={db_name} user={user} password={password}")
cur = conn.cursor()
query = 'select id,full_text from tweets_data'
cur.execute(query)
columns_cont = cur.fetchall()
conn.commit()
columns_cont_lst = [list(x) for x in columns_cont]


cleaned_up = list(map(regex_str,columns_cont_lst))

if __name__ == "__main__":
    with mp.Pool(8) as pool:
        result = pool.map(regex_updt,cleaned_up)