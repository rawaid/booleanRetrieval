__author__ = 'rawaid'

from index import make_index

def ui():
    indie = make_index()
    print("Choose Query Type:\n1: Single Token Query\n2: AND Query\n3: OR Query",
           "\n4: Phrase Query\n5: Near Query\n6: QUIT")
    uRes = input("Enter Query Type (1-6): ")
    uRes = int(uRes)
    if uRes == 1:
        query = input("Please enter a single word: ")
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