from tabulate import tabulate

import re
class bb3:
    def hater():
        Actualfailure=[]
        iter=0
        prevline=""
        errorcheck=open('shortenedlog.txt','r')
        errorcheker=errorcheck.read()
        aa=open('resultlog69.txt','w+')
        with open('shortenedlog.txt','r+') as f:
            for line in f:
                if "Caught"in line:
                    
                    Actualfailure.insert(iter,prevline)
                    iter+=1
                    
                
                    
                    nextline=next(f)
                    aa.write(line)
                    while("AETEST-3-ERROR") in nextline:
                        nextline=next(f)
                        aa.write(nextline)
                        if "AETEST-6" in nextline:
                            nextline=next(f)
                        if "result of testcase" in nextline:
                            aa.write(nextline)
               
                prevline=line
            
                        
                            
            aa.close()
        word='Failed.reason:(.*)'
        gg=open('resultlog69.txt')
        f=gg.read()
        bb=re.findall(word,f)
        #print(Actualfailure)
        actualfile=open('actually.txt','w')
        for x in range (len(Actualfailure)):
            actualfile.write(Actualfailure[x])
            actualfile.write("\n")
        actualfile.close()
        with open('actually.txt','r') as log:
            f=log.read()
        ShortenTextAeTestInfo='.%AETEST-6-INFO.+|'
        ShortenTextAetError='.%SCRIPT-3-ERROR.+|.%AETEST-3-ERROR..+|.NONE'
        ShortenListOfText=re.findall(ShortenTextAetError,f)
        shortenlogpart2=']:.+'
        #print(ShortenListOfText)
        shortenlistoftextpart2=re.findall(shortenlogpart2,f)
        print(shortenlistoftextpart2)
        return shortenlistoftextpart2
        
                
print(bb3.hater())
