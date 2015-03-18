__author__ = 'Nick'

from dbsandbox import *
import os
import pickle
from index import getLTC, getNNN
from nltk.stem.porter import PorterStemmer


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

def eval():
    indieNNN = getNNN()
    indieLTC = getLTC()
    for i in range(1, get_itemNum()):
        itemTitle = get_itemItem(i)
        releDic = genReleDic(itemTitle)
        print(releDic)

eval()


