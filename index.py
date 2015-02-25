__author__ = 'rawaid'

from dbsandbox import get_clean
from dbsandbox import get_size
import math
#from dbsandbox import

def make_index():
    fileNum = 1
    index = dict()
    numURL = get_size()
    while fileNum < numURL:
        cleanText = get_clean(fileNum)
        #print(cleanText)
        wordInd = 1
        docID = fileNum
        for item in cleanText:
            if item not in index:
                index[item] = dict()
            if docID not in index[item]:
                index[item][docID] = list()
            index[item]
            index[item][docID].append(wordInd)
            wordInd += 1

        fileNum += 1
    #print(index)
    return index

def getNNN():
    numURL = get_size()
    index = make_index()
    #docLen = dict()
    #for i in range(0, numURL):
       # docLen[i] = 0
    for term in index:
        #print("ITEM", term, "\n")
        docFreq = len(index[term].keys())
        #print('docfrq', docFreq)
        idf = math.log10(numURL/docFreq)
        for doc in index[term]:
            #print(doc)
            length=len(index[term][doc])
            #print('len', length)
            termFreq = 1+math.log(length)
            #print('doc', index[term][doc])
            index[term][doc][0] = termFreq
            #print('doclen', docLen[doc], '\n')
            #docLen[doc] += (termFreq*termFreq)
        #print('\n', termFreq)
    return index

def getLTC():
    numURL = get_size()
    index = make_index()
    docLen = dict()
    for i in range(0, numURL):
        docLen[i] = 0
    for term in index:
        #print("ITEM", term, "\n")
        docFreq = len(index[term].keys())
        #print('docfrq', docFreq)
        idf = math.log10(numURL/docFreq)
        for doc in index[term]:
            #print(doc)
            length=len(index[term][doc])
            #print('len', length)
            termFreq = 1+math.log(length)
            #print('doc', index[term][doc])
            index[term][doc][0]=termFreq*idf
            #print('doclen', docLen[doc], '\n')
            docLen[doc] += (termFreq*termFreq)
        #print('\n', termFreq)

    for term in index:
        for doc in index[term]:
            index[term][doc][0] = ((index[term][doc][0])/(math.sqrt(docLen[doc])))
            #print(index[term][doc][0])
    return index




#added comment
#make_index()
getLTC()




