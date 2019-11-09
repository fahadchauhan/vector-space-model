import glob
import json
import math
import re
from helping import checkStopwords

map = {}
smap={}

df = {}
idf = {}
words = list()


def createVSM():
    file1 = glob.glob("ShortStories/*")
    N=0
    s = set()
    for files in file1:
        N = N+1
        f = open(files, "r")

        x = files;
        y = x.split('\\')
        x = y[1].split('.')
        dnum = x[0]

        lines = f.readlines()

        for i in lines:
            i = re.sub(r"[^A-Za-z0-9 ]", "" , i)
            i =  i.lower()
            words = i.split()
            for j in words:
                check = checkStopwords(j)
                if check==0:
                    # print(map["dog"])
                    s.add(j)
                    if j not in map:
                        map[j] = {}
                        map[j] = {dnum:1}
                    else:
                        if dnum not in map[j]:
                            map[j].update({dnum:0})
                        freq = map[j][dnum]
                        freq = freq + 1
                        map[j][dnum] = freq
    for i in s:
        keys =map[i].keys()
        df[i] = keys.__len__()

    for i in s:
        key = df[i]
        idf[i] = math.log10(N/key)
    with open("idf.txt" , 'w+') as file:
        file.write(json.dumps(idf))

    for i in s:
        keys =map[i].keys()
        for j in keys:
            freq = map[i][j]
            tf = 1 + math.log10(freq)
            map[i][j] = tf

    for i in s:
        keys =map[i].keys()
        for j in keys:
            d = idf[i]
            t = map[i][j]
            map[i][j] = t*d;

    s = sorted(s)
    for i in s:
        smap[i] = map[i]

    with open("vsm.txt" , 'w+') as file:
        file.write(json.dumps(smap))

    return smap,idf

def loadVSM():
    f = open('vsm.txt', "r")
    lines = f.readlines()
    c = lines[0]
    map = json.loads(c)

    f = open('idf.txt', "r")
    lines = f.readlines()
    c = lines[0]
    idf = json.loads(c)
    return map,idf

def processQuery(query, map, idf):
    doc = {}
    qmap = {}
    qs = set()
    words = query.split()
    s = set()
    for i in map:
        s.add(i)
    s = sorted(s)

    # terms = str()
    # terms = ["" for x in range(words)]
    # for i in words:
    #     i = i.lower()
    #     check = checkStopwords(i)
    #     if check == 0:
    #         if i in map:
    #             terms.__add__(i)
    # words = terms

    for i in words:
        i = i.lower()
        check = checkStopwords(i)
        if check == 0:
            if i not in map:
                continue

            qs.add(i)
            if i not in qmap:
                qmap[i] = 1
            else:
                freq = qmap[i]
                freq = freq + 1
                qmap[i] = freq
    cos = [0] * 50
    if qs:
        for i in qs:
            freq = qmap[i]
            tf = 1 + math.log10(freq)
            # if i in idf:
            x = tf * idf[i]
            # else:
            #     print("Invalid Doc.")
            #     break
            qmap[i] = x     #tf-idf of query

        z =0;
        for j in range(1,51):
            doc[j] = {}
            for i in s:
                k = str(j)
                if k in map[i].keys():
                   doc[j].update({i: map[i][k]})
                else:
                    doc[j].update({i: 0})

        qu=0.0
        for i in qmap:
            x = qmap[i]
            x = x * x
            qu = qu + x
        qu = math.sqrt(qu)

        den = list()
        for i in range(1,51):
            x=0.0
            y=0.0
            for j in doc[i].keys():
                x = doc[i][j] * doc[i][j]
                x = x * x
                y = y + x
            y = math.sqrt(y)
            y = y * qu
            den.insert(i,y)

        # cos = [0]*50

        for i in range(1,51):
            num = 0.0
            for j in qmap:
                num = num + (qmap[j] * doc[i][j])
            x = num/den[i-1]
            cos[i-1] = x
    else:
        return cos,0
    return cos,1

