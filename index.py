__author__ = 'rawaid'

from dbsandbox import get_clean
from collections import defaultdict
#from dbsandbox import

def make_index():
    i = True
    fileNum = 1
    file = 1
    index = dict()
    while fileNum < 5:
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
    print(index)

make_index()

# class InvertedIndexModel:
#
#     # new basic dictionary
#     #invertedIndex = defaultdict(defaultdict())
#
#     def __init__(self, docID):
#         self.invertedIndex = defaultdict(lambda : defaultdict())
#         self.docID = docID
#         self.populateInvertedIndex()
#
#
#     def populateInvertedIndex(self):
#         tokenList = self.getTokensFromCleanFile()
#         return tokenList
#
#     def getTokensFromCleanFile(self):
#         fileName = self.getFileName()
#         fo = open(("data/clean/" + fileName), "r", encoding='latin1')
#
#         term = fo.readline()
#         i = 0
#         for term in fo:
#             if term not in self.invertedIndex:
#                 self.invertedIndex[term] = defaultdict(list)
#             if self.docID not in self.invertedIndex[term]:
#                 self.invertedIndex[term][self.docID].append(i)
#             i = i+1
#
#         fo.close()
#         return self.invertedIndex
#
#     def getFileName(self):
#         filename = str(self.docID)
#         # nameLength = len(filename)
#         # for i in range(abs(nameLength - 7)):
#         #     filename = "0" + filename
#
#         return filename + ".txt"
#
#
# def main():
#     for i in range(1,2):
#         docID = str(i)
#         ind = InvertedIndexModel(docID)
#         token = ind.populateInvertedIndex()
#         print(token)
#
# main()


