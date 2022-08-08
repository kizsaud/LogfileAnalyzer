import re
from table import tablemaker
def myfile(name):
    with open(name,'r') as log:
        f=log.read()
    ShortenTextAeTestInfo='.%AETEST-6-INFO.+|.%AETEST-3-ERROR.+|%GENIE-6-INFO:.+pyATS.+'
    ShortenTextAetError='.%AETEST-6-INFO.+|.%AETEST-3-ERROR..+'
    ShortenListOfText=re.findall(ShortenTextAeTestInfo,f)
    shortenlogpart2=']:.+'

    #write the shortened version to a file, Make this to a method, so it auto does this
    shortlog =open ('shortenedlog.txt','w+')
    for x in range (len(ShortenListOfText)):
        shortlog.write(ShortenListOfText[x])
        shortlog.write("\n")
    shortlog.close()
    with open('shortenedlog.txt','r') as log2:
        z=log2.read()
    shortenlistoftextpart2=re.findall(shortenlogpart2,z)


    results=open('new.txt','w')

    #this file is written simply because it makes the text easier to read, we took out anything that had cisco/time/etc
    for x in range(len(shortenlistoftextpart2)):
        results.write(shortenlistoftextpart2[x])
        results.write("\n")
    results.close()
myfile('k1.txt')
tablemaker()