# Testing Code to Print out DB Tables
#comment
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
        cleanRecord = str(record)
        cleanRecord = cleanRecord[2:-3]
        return cleanRecord

def get_url(idIn):
    #use id to lookup url in CachedURL
    cur.execute("SELECT url FROM CachedURL WHERE id = '%i'" % idIn)
    for record in cur.fetchall():
        cleanRecord = str(record)
        cleanRecord = cleanRecord[2:-3]
        return cleanRecord

def get_type(idIn):
    #use URLToItem to get item ID
    #use itemID to get the type
    '''
    cur.execute("SELECT type FROM Item WHERE id = '%i'" % idIn)
    for record in cur.fetchall():
        return(record)
    '''
    cur.execute("SELECT itemID FROM URLToItem WHERE id = '%i'" % idIn)
    for record in cur.fetchall():
        var = record
    cur.execute("SELECT type FROM Item WHERE id = '%i'" % var)
    for record in cur.fetchall():
        cleanRecord = str(record)
        cleanRecord = cleanRecord[2:-3]
        return cleanRecord

def get_item(idIn):
    #use itemID from URLToItem table
    #use itemID to get the name
    cur.execute("SELECT itemID FROM URLToItem WHERE id = '%i'" % idIn)
    for record in cur.fetchall():
        var = record
    cur.execute("SELECT name FROM Item WHERE id = '%i'" % var)
    for record in cur.fetchall():
        cleanRecord = str(record)
        cleanRecord = cleanRecord[2:-3]
        return cleanRecord



