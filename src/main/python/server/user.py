import os
import sqlite3
import pandas as pd

#Delete old user.db on start
if os.path.exists('user.db'):
    os.remove('user.db')

# Create DB
conn = sqlite3.connect('user.db')

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users (username varchar(255),email varchar(255), picture varchar(255))")
c.execute("insert into users values (?, ?,?)", ('gsingh','gsingh@student.tgm.ac.at','link.at'))
conn.commit()
conn.row_factory =sqlite3.Row
#CRUD functions
def sql_query(query):
    cur=conn.cursor()
    cur.execute(query)
    rows=cur.fetchall()
    return rows

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
    return rows