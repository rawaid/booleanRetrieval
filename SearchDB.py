__author__ = 'rawaid'
import sqlite3
class SearchDB:
    def __init__(self, dbfile):
        self.dbfile = dbfile
        self.cxn = sqlite3.connect(dbfile)
        self.cur = self.cxn.cursor()

    def getClean(self):

    def getTitle(self):

    def getURL(self):

    def getItemType(self):

    def getItemName(self):
