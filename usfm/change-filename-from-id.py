'''
Bulk Rename USFM files according to the ID of the book
'''
import os
import codecs
import re

projects = ["HIN", "GUJ", "MAR", "KHN"]

for prj in projects:
    EXT = ["usfm", "sfm", "ptx"]
    SOURCEDIR = "C:\\path\\to\\usfm"import os
    PROJECT = "-OA-" + prj
    bk = {"GEN":1, "EXO":2, "LEV":3, "NUM":4, "DEU":5, "JOS":6, "JDG":7, "RUT":8, "1SA":9, "2SA":10, "1KI":11, "2KI":12,\
          "1CH":13, "2CH":14, "EZR":15, "NEH":16, "EST":17, "JOB":18, "PSA":19, "PRO":20, "ECC":21, "SNG":22, "ISA":23,\
          "JER":24, "LAM":25, "EZK":26, "DAN":27, "HOS":28, "JOL":29, "AMO":30, "OBA":31, "JON":32, "MIC":33, "NAM":34,\
          "HAB":35, "ZEP":36, "HAG":37, "ZEC":38, "MAL":39,\
          # NT Starts here
          "MAT":40, "MRK":41, "LUK":42, "JHN":43, "ACT":44, "ROM":45, "1CO":46, "2CO":47, "GAL":48, "EPH":49, "PHP":50,\
          "COL":51, "1TH":52, "2TH":53, "1TI":54, "2TI":55, "TIT":56, "PHM":57, "HEB":58, "JAS":59, "1PE":60, "2PE":61,\
          "1JN":62, "2JN":63, "3JN":64, "JUD":65, "REV": 66}

    fileList = os.listdir(SOURCEDIR)
    try:
        os.mkdir(SOURCEDIR + "\\_out")
    except:
        shutil.rmtree(SOURCEDIR + "\\_out")
        os.mkdir(SOURCEDIR + "\\_out")
        
    for fil in fileList:
        b = fil.split(".")
        try:
            if(b[1].lower() in EXT):
                f = codecs.open(os.path.join(SOURCEDIR, fil), mode = 'r', encoding = 'utf-8')
                fc = f.read()
                f.close()

                try:
                    bkID = re.findall("\\id ([A-Z0-9]{3})", fc)[0]
                    bookNumber = bk[bkID]
                    if(bookNumber >= 40):
                        bookNumber += 1
                    fName = str(bookNumber).zfill(2) + "_" + bkID + PROJECT + "." + EXT[0]
                except:
                    fName=fil
                o = codecs.open(os.path.join(SOURCEDIR + "\\_out", fName), mode='w', encoding='utf-8')
                o.write("\\rem Original File Name: " + fil)
                o.write("\n\\rem Processed using USFM_Bulk_Rename_Utility by beniza\n")
                o.write(fc)
                o.close()
        except:
            pass
