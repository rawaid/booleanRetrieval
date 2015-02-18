__author__ = 'rawaid'

from dbsandbox import get_clean
#from dbsandbox import

def make_index():
    i = True
    file = 0
    index = dict()
    while i:
        cleanText = get_clean(file)
        wordInd = 0
        docID = file
        for word in cleanText:
            if word not in index:
                index[word] = dict()
            if docID not in index[word]:
                index[word][docID] = list()
            index[word]
            [docID].append(wordInd)
            wordInd += 1

        if cleanText is None:
            i = False
        else:
            file += 1


