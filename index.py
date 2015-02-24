__author__ = 'rawaid'

from dbsandbox import get_clean
from dbsandbox import get_size
from collections import defaultdict
#from dbsandbox import

def make_index():
    i = True
    fileNum = 1
    file = 1
    index = dict()
    numURL = get_size()
    while fileNum < numURL:
        cleanText = get_clean(fileNum)
        #print(cleanText)
        wordInd = 0
        docID = fileNum
        for item in cleanText:
            if item not in index:
                index[item] = dict()
            if docID not in index[item]:
                index[item][docID] = list()
            index[item]
            index[item][docID].append(wordInd)
            wordInd += 1

        if cleanText is None:
            i = False
        else:
            file += 1
        fileNum += 1
    #print(index)
    return index
#added comment
make_index()




