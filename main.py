import pandas as pd
import sqlalchemy as db
from dotenv import load_dotenv
import os
import tweepy

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN =  os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET =  os.getenv("ACCESS_TOKEN_SECRET")

'''
class post_connect:


    def __init__(self):    
        self.db_server = os.getenv("db_server")
        self.user = os.getenv("user")
        self.password = os.getenv("password")
        self.ip = os.getenv("ip")
        self.db_name = os.getenv("db_name")
        
    
    def conex(self):
        self.conex = db.create_engine(f'{self.db_server}://{self.user}:{self.password}@{self.ip}/{self.db_name}').connect()
    
    def update_db(self, url_db):
'''
#o.to_sql(name='wow',con=conex)

colunas = ['created_at','id','full_text','followers_count','friends_count','location','user_created_at']

auth = tweepy.AppAuthHandler(API_KEY, API_SECRET_KEY)

#auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    for tweet in tweepy.Cursor(api.search, q='Trump', tweet_mode="extended").items(1):
        x.append(tweet)

except:
    print('shits fucked mate')


conn = psycopg2.connect(f"host={ip}  dbname={db_name} user={user} password={password}")
cur = conn.cursor()
cur.execute("INSERT INTO tweets_data VALUES (%s, %s, %s, %s, %s, %s, %s)", (x[0]._json['created_at'],x[0]._json['id'],x[0]._json['full_text'],x[0]._json['user']['followers_count'],x[0]._json['user']['friends_count'],x[0]._json['user']['location'],x[0]._json['user']['created_at']))
conn.commit()    