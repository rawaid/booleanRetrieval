__author__ = 'rawaid'

from index import make_index
from dbsandbox import get_item, get_title, get_type, get_url
import sys
from nltk.stem.porter import PorterStemmer
from index import getNNN

def ui():
    indie = getNNN()
    print("Choose Query Type:\n1: Single Token Query\n2: AND Query\n3: OR Query",
           "\n4: Phrase Query\n5: Near Query\n6: QUIT")
    uRes = input("Enter Query Type (1-6): ")
    uRes = int(uRes)
    ps = PorterStemmer()
    if uRes == 1:
        query = input("Please enter a single word: ")
        query = ps.stem(query.lower())
        #print(query)
        singleTokenQ(query, indie)
    elif uRes == 2:
        fWord = input("Please enter first word: ")
        sWord = input("Please enter second word: ")
        fWord = ps.stem(fWord.lower())
        sWord = ps.stem(sWord.lower())
        andQ(fWord, sWord, indie)

    elif uRes == 3:
        fWord = input("Please enter first word: ")
        sWord = input("Please enter second word: ")
        fWord = ps.stem(fWord.lower())
        sWord = ps.stem(sWord.lower())
        orQ(fWord, sWord, indie)


    elif uRes == 4:
        fWord = input("Please enter first word: ")
        sWord = input("Please enter second word: ")
        fWord = ps.stem(fWord.lower())
        sWord = ps.stem(sWord.lower())
        phraseQ(fWord, sWord, 1, indie)

    elif uRes == 5:
        fWord = input("Please enter first word: ")
        sWord = input("Please enter second word: ")
        fWord = ps.stem(fWord.lower())
        sWord = ps.stem(sWord.lower())
        nearQ(fWord, sWord, 5, indie)

    elif uRes == 6:
        print("Thank you and have a nice day!")
        sys.exit()

    else:
        print("Try picking an option this time.  Did you think ", uRes, " was an option?\n\n")
        ui()


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
            print(i, ".  ", title, "\n    ", url, "\n    ", type, ": ", subject, "\n", sep='')
            i += 1
        ui()
    else:
        print("Query: ", query, " not found\n")
        ui()

def andQ(fWord, sWord, indie):
    if fWord in indie:
        if sWord in indie:
            fResults = indie[fWord]
            sResults = indie[sWord]
            fID = fResults.keys()
            andID = []
            i = 1
            for item in fID:
                if item in sResults:
                    andID.append(item)
            for item in andID:
                title = get_title(item)
                url = get_url(item)
                type = get_type(item)
                subject = get_item(item)
                print(i, ".  ", title, "\n    ", url, "\n    ", type, ": ", subject, "\n", sep='')
                i += 1
            ui()
        else:
            print(sWord, "not found\n")
            ui()
    else:
        print(fWord, "not found\n")
        ui()

def orQ(fWord, sWord, indie):
    if fWord or sWord in indie:
        if fWord in indie:
            fResults = indie[fWord]
        else:
            print(fWord, "not found")
            if sWord in indie:
                print("Running Single Token Query for:", sWord)
                singleTokenQ(sWord, indie)
            else:
                print(sWord, "not found")
                ui()

        if sWord in indie:
            sResults = indie[sWord]
        else:
            print(sWord, "not found")
            if fWord in indie:
                print("Running Single Token Query for:", fWord)
                singleTokenQ(fWord, indie)
            else:
                print(fWord, "not found")
                ui()

        fID = fResults.keys()
        sID = sResults.keys()
        mID = list(fID) + list(sID)
        mID = list(set(mID))
        i = 1
        for item in mID:
            title = get_title(item)
            url = get_url(item)
            type = get_type(item)
            subject = get_item(item)
            print(i, ".  ", title, "\n    ", url, "\n    ", type, ": ", subject, "\n", sep='')
            i += 1
        ui()
    else:
        print(fWord, "or", sWord, "not found\n")
        ui()

def phraseQ(fWord, sWord, dis, indie):
    if fWord in indie:
        if sWord in indie:
            fResults = indie[fWord]
            fVal = fResults.values()
            sResults = indie[sWord]
            sVal = sResults.values()
            idList = []

            fID = fResults.keys()
            andID = []
            for item in fID:
                if item in sResults:
                    andID.append(item)

            i = 1
            for item in andID:
                fInd = fResults[item]
                #print (fInd)
                sInd = sResults[item]
                nInd1 = str(fInd)
                nInd1 = nInd1[1:-1]
                #print(nInd1)
                nInd2 = str(sInd)
                nInd2 = nInd2[1:-1]
                #print("Index for word one:", nInd1, "\nIndex for word two:", nInd2)
                fBs = int(nInd2) - int(nInd1)
                #print (fBs)
                fBs = 0 < fBs < dis+1
                #print(fBs)
                if fBs:
                    idList.append(item)
            if not idList:
                print("Phrase:", fWord, sWord, "not found\n")
                ui()

            #print(idList)
            for item in idList:
                title = get_title(item)
                url = get_url(item)
                type = get_type(item)
                subject = get_item(item)
                print(i, ".  ", title, "\n    ", url, "\n    ", type, ": ", subject, "\n", sep='')
                i += 1
        ui()



def nearQ(fWord, sWord, dis, indie):
    if fWord in indie:
        if sWord in indie:
            fResults = indie[fWord]
            fVal = fResults.values()
            sResults = indie[sWord]
            sVal = sResults.values()
            idList = []

            fID = fResults.keys()
            andID = []
            for item in fID:
                if item in sResults:
                    andID.append(item)

            i = 1
            for item in andID:
                fInd = fResults[item]
                #print (fInd)
                sInd = sResults[item]
                nInd1 = str(fInd)
                nInd1 = nInd1[1:-1]
                #print(nInd1)
                nInd2 = str(sInd)
                nInd2 = nInd2[1:-1]
                #print("Index for word one:", nInd1, "\nIndex for word two:", nInd2)
                fBs = int(nInd1) - int(nInd2)
                sBf = int(nInd2) - int(nInd1)
                fBs = 0 < fBs < dis+1
                sBf = 0 < sBf < dis+1
                if fBs:
                    idList.append(item)
                if sBf:
                    idList.append(item)
            if not idList:
                print("Phrase:", fWord, sWord, "not found\n")
                ui()

            #print(idList)
            for item in idList:
                title = get_title(item)
                url = get_url(item)
                type = get_type(item)
                subject = get_item(item)
                print(i, ".  ", title, "\n    ", url, "\n    ", type, ": ", subject, "\n", sep='')
                i += 1
        ui()

ui()