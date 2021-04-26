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
import numpy as np
from tqdm import tqdm
from textblob import TextBlob


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
query = 'select DISTINCT key_id from tweets_data'
cur.execute(query)
tuples_query = cur.fetchall()
conn.commit()
personalities = [i[0] for i in tuples_query]

def blobing(text_ev):
    from textblob import TextBlob
    return [TextBlob(text_ev).sentiment[0], TextBlob(text_ev).sentiment[1]]


def sentiment_pers(kate):

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
    parser_q = re.sub('\'','',kate)
    to_que = f"SELECT full_text FROM tweets_data WHERE key_id = '{parser_q}'"
    cur.execute(to_que)
    tuples_q = cur.fetchall()
    comments = [q[0] for q in tuples_q]
    conn.commit()
    lista_q = list(map(blobing,comments))


    lista_pol = [q[0] for q in lista_q if q[0] != 0]
    lista_sub = [e[1] for e in lista_q if e[1] != 0]
    try:
        avg_pol = sum(lista_pol)/len(lista_pol)
        avg_sub = sum(lista_sub)/len(lista_sub)
    except ZeroDivisionError:
        avg_pol = 0
        avg_sub = 0


    conn = psycopg2.connect(f"host={ip}  dbname={db_name} user={user} password={password}")
    cur = conn.cursor()
    cur.execute("INSERT INTO sentiments VALUES (%s, %s, %s)", (kate ,avg_pol, avg_sub))
    conn.commit()

if __name__ == "__main__":
    with mp.Pool(8) as pool:
        kalua = pool.map(sentiment_pers,personalities)
    
