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
    file = open("data/clean/"+item+".txt", encoding='latin')
    cleanText = file.read()
    #print(cleanText)
    #print(item)
    #print(type(cleanText))
    cleanText = cleanText.split()
    return cleanText

def get_title(idIn):
    #use id to lookup title in CachedURL
    cur.execute("SELECT title FROM CachedURL WHERE id = '%i'" % idIn)
    for record in cur.fetchall():
        print(record)

def get_url(id):
    #use id to lookup url in CachedURL
    return None

def get_type(id):
    #use urlToItem to get itemID
    #use item table to get type
    return None

def get_item(id):
    #use urlToItem to get itemID
    #use item table to get item name
    return None





#get_items()
#get_urls()
#get_clean(4)
get_title(1)