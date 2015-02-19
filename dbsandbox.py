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

def get_title(id):
    #use id to lookup title in CachedURL

def get_url(id):
    #use id to lookup url in CachedURL

def get_type(id):
    #use urlToItem to get itemID
    #use item table to get type

def get_item(id):
    #use urlToItem to get itemID
    #use item table to get item name





#get_items()
#get_urls()
get_clean(4)