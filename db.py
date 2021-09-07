import os
import creds

username = creds.db['username']
password = creds.db['password']
db_name = creds.db['name']


def backup_db():
    os.environ["MYSQL_PWD"] = password
    os.system('mysqldump -u '+username+' '+db_name+' > '+db_name+'.sql')
    os.environ["MYSQL_PWD"] = 'token'

def load_db():
    os.environ["MYSQL_PWD"] = password
    os.system('mysql -u '+username+' '+db_name+' < '+db_name+'.sql')
    os.environ["MYSQL_PWD"] = 'token'
