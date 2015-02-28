__author__ = 'Nick'

from index import getLTC, getNNN
from dbsandbox import get_item, get_title, get_type, get_url, get_size
import sys
from nltk.stem.porter import PorterStemmer
from collections import Counter


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
    uQuery = input("Enter Query of 'QUIT': ")
    qDict = dict()
    scores = dict()
    if uQuery == 'QUIT':
        print("Thank for your time, Laurence. Have a lovely day.")
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
            for word in uQuery:
                word = ps.stem(word.lower())
                qDict[word] += 1
                print('you are query:', word)
                #print(qDict[word])


                #for i in range(0, len(uQuery)):
                if word in indie:
                    print('Getting search results for', word)
                    # print(indie[word], "/n")
                    for docID in indie[word].keys():
                        # docVal = str(len(indie[word][docID])
                        # docVal = int(docVal[1:-1])
                        docVal = len(indie[word][docID])
                        scores[docID] = qDict[word]*docVal
                        # print("docVal", docID, indie[word][docID])
                        # print(qDict[word])
                        # print(scores[docID])
                results = Counter(scores)
                        #results.most_common()
                i = 1
            for k, v in results.most_common(5):
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
                print('you are query:', word)

            #for i in range(0, len(uQuery)):
                if word in indie:
                   print('Getting search results for', word)
                   print(indie[word],"/n")
                   print('bah', indie[word].values())


rrUI()