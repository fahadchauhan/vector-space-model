import re

def checkStopwords(term):
    f = open('Stopword-List.txt','r')
    stops = f.readlines()
    check =0
    for i in stops:
        i = re.sub(r"\n", "", i)
        if term == i:
            check = 1
            break
    return check