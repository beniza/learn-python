'''
This program tests the completeness of the token list against the usfm
files from the tokens created. This will help us in testing if any words or
phrases that are not correctly represented in the token list.

    Input: usfm files (under the usfm folder)
           token file (in this case ROM-REV_Full.csv)
    Output: usfm files after replacing the words in token file with "". This
            will get stored in the 'out' folder
'''

import codecs
import os

fileList = os.listdir("usfm\\")

tokenFile = codecs.open("ROM-REV_Full.csv", mode='r', encoding="utf-8")
tokens = tokenFile.readlines()

# Sorting the tokens in the reverse order to prevent smaller words get replaced before the longer ones.
tokens = sorted(tokens, key=len, reverse=True) 

for fil in fileList:
    b=fil.split(".")
    bk = b[0]

    if b[1]=="usfm":
        f = codecs.open("usfm\\" + fil, mode = "r", encoding = "utf-8")
        fc = f.read()
        f.close()

        #Replacing the matching tokens with ""
            #We can modify this step and can get a usfm file translated
            #into a new language if the translation of the tokens available.
        for token in tokens:
            fc = fc.replace(token.strip("\n"), "")
        
        o = codecs.open("out\\" + fil, mode="w", encoding="utf-8")
        o.write(fc)
        o.close()
