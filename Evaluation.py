__author__ = 'Nick'

from dbsandbox import *
from index import getLTC, getNNN
from nltk.stem.porter import PorterStemmer
import random
import math
import operator
from collections import Counter


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

def genNNN(indie, itemTitle):
    ps = PorterStemmer()
    if itemTitle.find(':') !=-1:
        itemTitle = itemTitle.replace(":", "")
    if itemTitle.find(',') !=-1:
        itemTitle = itemTitle.replace(",", "")
    if itemTitle.find("'") !=-1:
        itemTitle = itemTitle.replace("'", "")
    qDict = dict()
    scores = dict()
    query = str.split(itemTitle)
    for word in query:
        qDict[ps.stem(word.lower())] = 0
    for docID in range(1, get_size()+1):
        scores[docID] = .00000000001 * random.random()
    for word in query:
        word = ps.stem(word.lower())
        qDict[word] += 1

        if word in indie:
            for docID in indie[word].keys():
                docVal = indie[word][docID][0]
                scores[docID] = qDict[word]*docVal
    scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    sList = dict()
    i = 1
    for key, val in scores:
        sList[i] = key
        i += 1
    print("NN sLIST", sList)
    print("NN scores", scores)
    #print(scores[0][0])
    return sList

def genLTC(indie, itemTitle):
    ps = PorterStemmer()
    if itemTitle.find(':') !=-1:
        itemTitle = itemTitle.replace(":", "")
    if itemTitle.find(',') !=-1:
        itemTitle = itemTitle.replace(",", "")
    if itemTitle.find("'") !=-1:
        itemTitle = itemTitle.replace("'", "")
    qDict = dict()
    scores = dict()
    query = str.split(itemTitle)
    for word in query:
        qDict[ps.stem(word.lower())] = 0
    for docID in range(1, get_size()+1):
        scores[docID] = .00000000001 * random.random()
    for word in query:
        word = ps.stem(word.lower())
        qDict[word] += 1

    if word in indie:
        for docID in indie[word].keys():
            docVal = indie[word][docID][0]
            for word in query:
                word = ps.stem(word.lower())
                if qDict[word] == 0:
                    l = 0
                else:
                    l = 1 + math.log(qDict[word]+1)
                t = l * math.log((get_size()/len(indie[word].keys()))+1)
                for item in qDict.keys():
                    mag = math.sqrt((1+math.log(qDict[item]+1)) * (get_size()/len(qDict.keys())))
                c = t/mag
                qDict[word] = c
                scores[docID] = qDict[word]*docVal

    #scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    sList = dict()
    scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    i = 1
    for key, val in scores:
        sList[i] = key
        i += 1

    print("LTC sLIST", sList)
    print("LTC scores", scores)

    return sList

def getPrec(scores, rVal):
    prec = 0
    for i in range(1, rVal):
        if scores[i] == 1:
            prec += 1
    prec = prec/rVal
    return prec


def eval():
    indieNNN = getNNN()
    indieLTC = getLTC()
    nnPten=nlPten=lnPten=llPten=nnPr=nlPr=lnPr=llPr=0
    nnMAP=nlMAP=lnMAP=llMAP=nnAUC=nlAUC=lnAUC=llAUC=0
    for i in range(1, get_itemNum()):
        itemTitle = get_itemItem(i)
        releDic = genReleDic(itemTitle)
        #GETTING NNN.NNN
        rVal = 1
        for i in releDic.keys():
            if releDic[i] == 1:
                rVal += 1
        print("nn")
        nnScore = genNNN(indieNNN, itemTitle)
        print("nl")
        nlScore = genLTC(indieNNN, itemTitle)
        print("ln")
        lnScore = genNNN(indieLTC, itemTitle)
        print("ll")
        llScore = genLTC(indieLTC, itemTitle)

        nnPten += getPrec(nnScore, 10)
        nnPr += getPrec(nnScore, rVal)

        #getMAP
        #getAUC




        #print(releDic)

eval()


