import pandas as pd
import sqlalchemy as db
from dotenv import load_dotenv
import os

load_dotenv()


db_server = os.getenv("db_server")
user = os.getenv("user")
password = os.getenv("password")
ip = os.getenv("ip")
db_name = os.getenv("db_name")


class post_connect(self):


    def __init__(self):
        
        db_server = os.getenv("db_server")
        user = os.getenv("user")
        password = os.getenv("password")
        ip = os.getenv("ip")
        db_name = os.getenv("db_name")

        conex = db.create_engine(f'{db_server}://{user}:{password}@{ip}/{db_name}').connect()

#o.to_sql(name='wow',con=conex)