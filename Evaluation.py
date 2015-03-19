__author__ = 'Nick'

from dbsandbox import *
import os
import pickle
from index import getLTC, getNNN
from nltk.stem.porter import PorterStemmer
import random


def genReleDic(item):
    releDic = dict()
    itemID = get_IDfromItem(item)
    for i in range(1, get_size()+1):
        releDic[i] = 0
    for i in range(1, get_size()+1):
        docItemID = get_itemIDfromID(i)
        if itemID == docItemID:
            releDic[i] = 1
        else:
            releDic[i] = 0
    return releDic

def genNN(releDic, indieNNN, itemTitle):
    ps = PorterStemmer()
    if itemTitle.find(':') !=-1:
        itemTitle = itemTitle.replace(":", "")
    qDict = dict()
    scores = dict()
    query = str.split(itemTitle)
    for word in query:
        qDict[ps.stem(word.lower())] = 0
    for docID in range(1, get_size()+1):
        scores[docID] = random.uniform(.0000000000001, .0000000000002)
    for word in query:
        word = ps.stem(word.lower())
        qDict[word] += 1

        if word in indieNNN:
            for docID in indieNNN[word].keys():
                docVal = indieNNN[word][docID][0]
                scores[docID] = qDict[word]*docVal
    print(scores)

def eval():
    indieNNN = getNNN()
    indieLTC = getLTC()
    for i in range(1, get_itemNum()):
        itemTitle = get_itemItem(i)
        releDic = genReleDic(itemTitle)
        #GETTING NNN.NNN
        genNN(releDic, indieNNN, itemTitle)
        print(releDic)

eval()


