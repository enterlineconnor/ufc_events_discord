import sqlalchemy
from sqlalchemy.sql.functions import user
from sqlalchemy.sql.sqltypes import Date
import creds
import db

username = creds.db['username']
password = creds.db['password']
db_name = creds.db['name']
host = creds.db['host']
port = creds.db['port']

from sqlalchemy import Table, Column, Integer, String, MetaData

engine = sqlalchemy.create_engine('mysql://'+username+':'+password+'@'+host+':'+str(port)) # connect to server
try:
    db.backup_db()
    engine.execute("DROP database "+db_name) #create db
except:
    print('DB Does Not Exist')

engine.execute("CREATE DATABASE "+db_name) #create db
engine.execute("USE "+db_name) # select new db
# use the new db
# continue with your work...
meta = MetaData()

events = Table(
    'events', meta, 
    Column('id', Integer, primary_key = True), 
    Column('name', String(255)), 
    Column('date', Date),
    Column('source', String(255)), 
)

meta.create_all(engine)

db.load_db()
