__author__ = 'Nick'

from index import getLTC, getNNN
from dbsandbox import *
import sys
from nltk.stem.porter import PorterStemmer
from collections import Counter
import math


def rrUI():
    print("WELCOME TO GOOGLE\nBrought to you by Nick & Ali")
    print("Supported Variants 'nnn' and 'ltc'(default is 'ltc')")
    dNorm = input("Please enter SMART variant for documents: ")
    qNorm = input("Please enter SMART variant for queries: ")
    print("Loading Index (Weight = ", dNorm, ")...", sep='')
    print("Calculating TFIDF weights...")
    if dNorm == 'nnn':
        indie = getNNN()
    else:
        indie = getLTC()
    print("Query Weighting Scheme:", qNorm)
    print("\n--------------------------------------------------------------")
    uQuery = input("Enter Query or 'QUIT': ")
    qDict = dict()
    scores = dict()
    if uQuery == 'QUIT' or uQuery == 'quit':
        print("Thank for your time, Doug. Have a lovely day.")
        sys.exit()
    else:
        ps = PorterStemmer()
        uQuery = str.split(uQuery)
        #print(type(uQuery))
        for word in uQuery:
            qDict[ps.stem(word.lower())] = 0
        for docID in range(1, get_size()+1):
            scores[docID] = 0
        if qNorm == 'nnn':
            print('Getting search results for', uQuery, "\n")
            for word in uQuery:
                word = ps.stem(word.lower())
                qDict[word] += 1
                #print('you are query:', word)
                #print(qDict[word])


                #for i in range(0, len(uQuery)):
                if word in indie:
                    # print(indie[word], "/n")
                    for docID in indie[word].keys():
                        # docVal = str(len(indie[word][docID])
                        # docVal = int(docVal[1:-1])
                        docVal = indie[word][docID][0] #(indie[word][docID])
                        scores[docID] = qDict[word]*docVal
                        # print("docVal", docID, indie[word][docID])
                        # print(qDict[word])
                        # print(scores[docID])

            results = Counter(scores)
            #print(results)
            #print(scores)
            i = 1
            itemDict = dict()
            for q in range(1, get_itemNum()):
                itemDict[q] = 0
            for key in range(1, get_size()):
                #print(key)
                #theID = get_IDfromTitle(key)
                itemKey = get_itemID(key)
                itemDict[itemKey] += scores[key]

            itemRes = Counter(itemDict)
            print("Item Search Results:")
            for key, val in itemRes.most_common(5):
                #theID = get_IDfromTitle(doc)
                type = get_typeItem(key)
                subject = get_itemItem(key)
                itemScore = itemDict[key]
                print(i, ".\t", type, ": ", subject, "\t(", itemScore, ")", sep="")
                i += 1

            i = 1
            print("\nURL Search Results")
            for k, v in results.most_common(5):
                #print (k)
                sTitle = get_title(k)
                sURL = get_url(k)
                sSubject = get_item(k)
                sType = get_type(k)
                print(i, ".\t", sTitle, "  (", v, ")\n\t", sURL, "\n\t", sType, ": ", sSubject, "\n", sep='')
                i+=1
            print("\n")
            #print(qDict)
            #print(scores)
            rrUI()
        else:
            for word in uQuery:
                word = ps.stem(word.lower())
                #print('you are query:', word)
                qDict[word] += 1



            #for i in range(0, len(uQuery)):
            if word in indie:
                print('Getting search results for', uQuery,"\n")
                for docID in indie[word].keys():
                    docVal = indie[word][docID][0]
                    #print(docVal)
                    for word in uQuery:
                        word = ps.stem(word.lower())
                        #print(qDict[word])
                        #print (word)
                        if qDict[word] == 0:
                            l = 0
                        else:
                            l = 1+math.log(qDict[word]+1)
                        t = l*math.log((get_size()/len(indie[word].keys()))+1)  #len(qDict.keys()))+1)
                        for item in qDict.keys():
                            mag = math.sqrt((1+math.log(qDict[item]+1))*(get_size()/len(qDict.keys())))
                        c = t/mag
                        qDict[word] = c
                        scores[docID] = qDict[word]*docVal
            results = Counter(scores)
            i = 1
            itemDict = dict()
            for q in range(1, get_itemNum()):
                itemDict[q] = 0
            for key in range(1, get_size()):
                #print(key)
                #theID = get_IDfromTitle(key)
                itemKey = get_itemID(key)
                itemDict[itemKey] += scores[key]

            itemRes = Counter(itemDict)
            print("Item Search Results:")
            for key, val in itemRes.most_common(5):
                #theID = get_IDfromTitle(doc)
                type = get_typeItem(key)
                subject = get_itemItem(key)
                itemScore = itemDict[key]
                print(i, ".\t", type, ": ", subject, "\t(", itemScore, ")", sep="")
                i += 1

            i = 1
            print("\nURL Search Results")
            for k, v in results.most_common(5):
                sTitle = get_title(k)
                sURL = get_url(k)
                sSubject = get_item(k)
                sType = get_type(k)
                val = scores[k]
                print(i, ".\t", sTitle, "  (", val, ")\n\t", sURL, "\n\t", sType, ": ", sSubject, "\n", sep='')
                i += 1
            print("\n")
            #print(qDict)
            #print(scores)
            rrUI()
                       #scores[docID] =  qDict[word]*docVal
                   # print(indie[word], "/n")
                   # print('bah', indie[word].values())


rrUI()