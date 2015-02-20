__author__ = 'rawaid'

from index import make_index
from dbsandbox import get_item, get_title, get_type, get_url
import sys

def ui():
    indie = make_index()
    print("Choose Query Type:\n1: Single Token Query\n2: AND Query\n3: OR Query",
           "\n4: Phrase Query\n5: Near Query\n6: QUIT")
    uRes = input("Enter Query Type (1-6): ")
    uRes = int(uRes)
    if uRes == 1:
        query = input("Please enter a single word: ")
        singleTokenQ(query, indie)

    elif uRes == 2:
        fWord = input("Please enter first word: ")
        sWord = input("Please enter second word: ")
        andQ(fWord, sWord, indie)

    elif uRes == 3:
        fWord = input("Please enter first word: ")
        sWord = input("Please enter second word: ")
        orQ(fWord, sWord, indie)


    elif uRes == 4:
        fWord = input("Please enter first word: ")
        sWord = input("Please enter second word: ")
        nearQ(fWord, sWord, 1, indie)

    elif uRes == 5:
        fWord = input("Please enter first word: ")
        sWord = input("Please enter second word: ")
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
    if fWord and sWord in indie:
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
        print(fWord, "or", sWord, "not found\n")
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
                return -1

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

def nearQ(fWord, sWord, dis, indie):
    if fWord and sWord in indie:
        fResults = indie[fWord]
        sResults = indie[sWord]
        fID = fResults.keys()
        andID = []
        for item in fID:
            if item in sResults:

                andID.append(item)
        for item in andID:
            title = get_title(item)
            url = get_url(item)
            type = get_type(item)
            subject = get_item(item)

    else:
        print(fWord, "and", sWord, "not found")
        ui()





ui()