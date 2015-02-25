__author__ = 'Nick'

from index import getLTC, getNNN
from dbsandbox import get_item, get_title, get_type, get_url
import sys
from nltk.stem.porter import PorterStemmer


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
    if uQuery == 'QUIT':
        print("Thank for your time, Laurence. Have a lovely day.")
        sys.exit()
    else:
        ps = PorterStemmer()

        uQuery = str.split(uQuery)
        print(type(uQuery))
        for word in uQuery:
            word = ps.stem(word.lower())
            print('yr query:', word)

        #for i in range(0, len(uQuery)):
            if word in indie:
               print('Getting search results for', word)
               print(indie[word], '/n')











rrUI()