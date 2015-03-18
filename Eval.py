__author__ = 'Nick'

from dbsandbox import *
import os
import pickle
from index import make_index
from nltk.stem.porter import PorterStemmer

def queryGrabber():
    numURL = get_size()
    releDic = dict()
    if os.path.exists("data/index.p"):
        indie = pickle.load(open("data/index.p", "rb"))
    else:
        make_index()
        indie = pickle.load(open("data/index.p", "rb"))

    for i in range(1, numURL+1):
        releDic[i] = 0
    numItem = get_itemNum()
    for i in range(1, numItem):
        uQuery = get_itemItem(i)
        releDocs = multiTokenQ(uQuery, indie)


def multiTokenQ(uQuery, indie):
    uQuery = str.split(uQuery)
    docList = list()
    ps = PorterStemmer()
    for word in uQuery:
        print(word)
        word = ps.stem(word.lower())
        docList += singleTokenQ(word, indie)
    docList = set(docList)
    print(docList)


def singleTokenQ(query, indie):
    if query in indie:
        results = indie[query]
        #print(results)
        docIDs = results.keys()
        #print(docIDs)
        i = 1
        for item in docIDs:
            title = get_title(item)
            url = get_url(item)
            type = get_type(item)
            subject = get_item(item)
            #print(i, ".  ", title, "\n    ", url, "\n    ", type, ": ", subject, "\n", sep='')
            i += 1
        return docIDs
    else:
        print("Query: ", query, " not found\n")
        return "0"


def evalPrinter():
    print("P@10\tP@R\tMAP\tAUC\nEvaluating: nnn.nnn\n")


queryGrabber()