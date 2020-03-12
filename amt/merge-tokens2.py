'''
Given an order of the books, this script will create a new list of tokens
which will not repeate the already found tokens in a previous book. Useful when
user wanted to translate the books in a specific order.

    INPUT: Order of the books (Currently alphabetical order. To be implemented)
    OUTPUT: tokenList.txt (A file with all the tokens with a unique number and
                           the list of books where the tokens in found)
            out\*.csv (Tokens of each file according to the order.                
'''

import codecs
import os

fileList = os.listdir(".\_in")

tok={}
i=1

for fil in fileList:
    b = fil.split(".")
    if(b[1]=="CSV"):
        bk = b[0]
        f=codecs.open("_in\\" + fil, mode="r", encoding="utf-8")
        fc = f.readlines()
        f.close() 
        fo = codecs.open("_out\\" + fil, mode="w", encoding="utf-8")
        for t in fc:
            try:
                tok[t.strip("\n")].append(bk)
                #fo.write(tok[t.strip("\n")[0]] + "\t" + t)
            except:
                tok[t.strip("\n")]= ["HIN" + str(i).zfill(5), bk]
                fo.write("Hin" + str(i).zfill(5) + "\t" + t)
                i += 1

fo.close()
o = codecs.open("tokenList.txt", mode="w", encoding="utf-8")
for k,v in tok.items():
    o.write(str(k) + "\t" + str(v) + "\n")

o.close()
