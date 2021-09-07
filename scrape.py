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

events =  requests.get("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
events_soup = BeautifulSoup(events.content, 'html.parser')

links = []
for link in events_soup.find_all('a'):
    links.append(link.get('href'))


for l in links:
    # print(l)
    if '/events/' in l and 'UFC' in l:
        # https://www.sherdog.com/events/UFC-Fight-Night-192-Smith-vs-Spann-89440
        individual = requests.get('https://www.sherdog.com'+l)
        individual_soup = BeautifulSoup(individual.content, 'html.parser')
        date = individual_soup.find_all(class_='date')[1].meta['content']
        # print(date)
        date = str(date).split('T')
        print(date[0])
        datetime_object = datetime.strptime(date[0], '%Y-%m-%d')
        # date = date.replace(",", "")
        # print(date)
        # datetime_object = datetime.strptime(date, '%B %d %Y')
        # print('===============================================')
        sherdog_link = 'https://www.sherdog.com'+l
        query = (f'INSERT INTO events (date,name,source) VALUES (\'{datetime_object}\',\'{individual_soup.title.contents[0]}\',\'{sherdog_link}\');')  
        engine.execute(query) #create db
        print(individual_soup.title.contents[0])
        print(datetime_object)
        print('https://www.sherdog.com'+l)
        print('===============================================')


