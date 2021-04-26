import pandas as pd
import sqlalchemy as db
from dotenv import load_dotenv
import os
import tweepy
import psycopg2
import multiprocessing as mp
import logging
import time

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
