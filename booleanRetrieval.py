__author__ = 'rawaid'

from index import make_index
from dbsandbox import get_item, get_title, get_type, get_url

def ui():
    indie = make_index()
    print("Choose Query Type:\n1: Single Token Query\n2: AND Query\n3: OR Query",
           "\n4: Phrase Query\n5: Near Query\n6: QUIT")
    uRes = input("Enter Query Type (1-6): ")
    uRes = int(uRes)
    if uRes == 1:
        query = input("Please enter a single word: ")
        if query in indie:
            results = indie[query]
            print(results)
            docIDs = results.keys()
            print(docIDs)
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
    elif uRes == 2:
        fWord = input("Please enter first word: ")
        sWord = input("Please enter second word: ")
    elif uRes == 3:
        fWord = input("Please enter first word: ")
        sWord = input("Please enter second word: ")
    elif uRes == 4:
        query = input("Please enter phrase: ")
    elif uRes == 5:
        fWord = input("Please enter first word: ")
        sWord = input("Please enter second word: ")
    elif uRes == 6:
        print("Thank you and have a nice day!")

    else:
        print("Try picking an option this time.  Did you think ", uRes, " was an option?\n\n")
        ui()

ui()