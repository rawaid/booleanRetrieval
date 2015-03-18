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


def get_size():
    cur.execute("SELECT * FROM CachedURL")
    num=0
    for record in cur.fetchall():
        num+=1
    return num

def get_itemNum():
    cur.execute("SELECT * FROM Item")
    num=0
    for record in cur.fetchall():
        num+=1
    #print(num)
    return num

def get_itemID(idIn):
    cur.execute("SELECT itemID FROM URLToItem WHERE id = '%i'" % idIn)
    for record in cur.fetchall():
        var = record
        var = str(var)
        var = int(var[1:-2])
        return var


def get_IDfromTitle(title):
    cur.execute("SELECT id from CachedURL where title = '%s'" % title)
    for record in cur.fetchall():
        #print(record)
        record = str(record)
        record = int(record[1:-2])
        #print(record)
        return record

def get_typeItem(idIn):
    cur.execute("SELECT type FROM Item WHERE id = '%i'" % idIn)
    for record in cur.fetchall():
        cleanRecord = str(record)
        cleanRecord = cleanRecord[2:-3]
        return cleanRecord

def get_itemItem(idIn):
    cur.execute("SELECT name FROM Item WHERE id = '%i'" % idIn)
    for record in cur.fetchall():
        cleanRecord = str(record)
        cleanRecord = cleanRecord[2:-3]
        print(cleanRecord)
        return cleanRecord
def get_IDfromItem(itemIn):
    cur.execute("SELECT id FROM Item WHERE name = '%s'" % itemIn)
    for record in cur.fetchall():
        record = str(record)
        record = int(record[1:-2])
        #print(record)
        return record
def get_itemIDfromID(idIn):
    cur.execute("SELECT itemID from URLToItem WHERE id = '%i'" % idIn)
    for record in cur.fetchall():
        record = str(record)
        record = int(record[1:-2])
        #print(record)
        return record

#get_IDfromTitle("A Tale of Two Cities - Wikipedia, the free encyclopedia")
#get_itemItem(5)
#get_IDfromItem("The Little Prince")
#get_itemIDfromID(465)
