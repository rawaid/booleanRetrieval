# Testing Code to Print out DB Tables

import sqlite3 as lite

conn = lite.connect('data/cache.db')
cur = conn.cursor()

def get_items():
    cur.execute("SELECT * FROM Item")
    for record in cur.fetchall():
        print(record)

def get_urls():
    cur.execute("SELECT * FROM CachedURL")
    for record in cur.fetchall():
        print(record)

def get_clean(item):
    #cur.execute("SELECT id FROM CachedURL WHERE url='%s'" % urlIn)
    #item = cur.fetchone()
    item = str(item)
    file = open("data/clean/"+item+".txt")
    cleanText = file.read()
    #print(item)
    #print(cleanText)
    return cleanText





#get_items()
#get_urls()
get_clean(4)