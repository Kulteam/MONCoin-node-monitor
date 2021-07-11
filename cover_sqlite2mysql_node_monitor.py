# coding=utf-8
import mysql.connector
import os

from mysql.connector import errorcode

config = {
  'user': 'your_username',
  'password': 'your_password',
  'host': 'your_host',
  'database': 'your_database',
  'raise_on_warnings': True
}

sqlite3path = "node_monitor.sqlite3"
database = "your_database"
host="your_host"
username="your_username"
password="your_password"

try:
  cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Access denied")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

drop_table= "DROP TABLE IF EXISTS nodes, node_polling"
cnx._execute_query(drop_table)


cover_sqlite3_to_mysql = "sqlite3mysql -f "+ sqlite3path +" --mysql-database "+database+" -h "+host+" -u "+username+" --mysql-password "+password
print(cover_sqlite3_to_mysql)
runScript=os.popen(cover_sqlite3_to_mysql)
showStatus=os.read()