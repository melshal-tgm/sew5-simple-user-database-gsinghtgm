import os
import sqlite3
import json
#Delete old user.db on start
if os.path.exists('user.db'):
    os.remove('user.db')

# Create DB
conn = sqlite3.connect('user.db')

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (username varchar(255),email varchar(255), picture varchar(255))")
cur.execute("insert into users values (?, ?,?)", ('gsingh','gsingh@student.tgm.ac.at','link.at'))
cur.execute("insert into users values (?, ?,?)", ('gsingh123','gsingh123@student.tgm.ac.at','link123.at'))
cur.execute("insert into users values (?, ?,?)", ('gsingh321','gsingh321@student.tgm.ac.at','link321.at'))
conn.commit()
conn.row_factory =sqlite3.Row

users=[]
#CRUD functions
def sql_query(query):
    cur=conn.cursor()
    cur.execute(query)
    rows=cur.fetchall()
    for row in rows:
        users.append([x for x in row])
    return json.dumps({'users':users})

def sql_edit_insert(query,var):
    cur=conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query, var)

def sql_query2(query,var):
    cur=conn.cursor()
    cur.execute(query,var)
    rows=cur.fetchall()
    for row in rows:
        users.append([x for x in row])
    return json.dumps({'users':users})