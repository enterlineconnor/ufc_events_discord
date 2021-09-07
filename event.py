from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
import sqlalchemy
from sqlalchemy.sql.functions import user
import creds
import db
from sqlalchemy import Table, Column, Integer, String, MetaData
from datetime import datetime

username = creds.db['username']
password = creds.db['password']
db_name = creds.db['name']
host = creds.db['host']
port = creds.db['port']

engine = sqlalchemy.create_engine('mysql://'+username+':'+password+'@'+host+':'+str(port)) # connect to server
engine.execute("USE "+db_name)

def next_event():
    result = engine.execute('select * from events WHERE `date` > NOW() group by name ORDER BY date asc limit 1;')
    event_name = ''
    for r in result:
        print(r['name'])
        print(r['date'])
        event_name = r['name']
    return event_name

def upcoming_events():
    result = engine.execute('select * from events WHERE `date` > NOW() group by name ORDER BY date asc')
    upcoming_list = '>>> '
    for r in result:
        print(r)
        r_id = str(r['id'])
        name = r['name'] 
        date = str(r['date'])
        upcoming_list += (name + '\nDate: ' +date + '\n' + '============================' + '\n')
    return upcoming_list