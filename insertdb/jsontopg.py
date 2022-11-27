import json
import psycopg2
from operator import ifloordiv
import os
from dotenv import load_dotenv
import time as t
import ip

t.sleep(15)

load_dotenv()
db = os.getenv("POSTGRES_DB")
us = os.getenv("POSTGRES_USER")
passw = os.getenv("POSTGRES_PASSWORD") 
ht = os.getenv("POSTGRES_HOST")

conn = psycopg2.connect(
    database= db,
    user = us,
    password = passw,
    host = ht
)
cur = conn.cursor()

with psycopg2.connect(
    database= db,
    user = us,
    password = passw,
    host = ht
) as conn:
    with conn.cursor() as cur:
        with open('output.json') as my_file:
            data = json.load(my_file)
            cur.execute(""" create table if not exists palabras(palabra text, par varchar(50)) """)
            query_sql = """ insert into palabras
                select * from json_populate_recordset(NULL::palabras, %s) """
            cur.execute(query_sql, (json.dumps(data),))