from tabulate import tabulate

import re
class LibraryGrabber:
    def LibraryGrab():
        prevline=""
        errorcheck=open('shortenedlog.txt','r')
        shortversion=[]
        count=0
        errorcheker=errorcheck.read()
        aa=open('resultlog.txt','r+')
        with open('shortenedlog.txt','r+') as f:
            for line in f:
                if "Caught an assertion"in line or "Caught error while" in line:
                    shortversion.insert(count,prevline)
                    count+=1
                    nextline=next(f)
                    aa.write(line)
                    while("AETEST-4-WARNING") in nextline or ("ASYNC_-3-ERROR") in nextline:
                        nextline=next(f)
                        aa.write(nextline)
                        if "AETEST-4-WARNING" in nextline:
                            nextline=next(f)
                        if "result of" in nextline:
                            aa.write(nextline)
                prevline=line
                            
                    
                      
                
                    
            
                        
                            
                        
        aa.close()
        with open('resultlog.txt','r') as log:
            f=log.read()
        ShortenTextAeTestInfo='.%AETEST-6-INFO.+|.%AETEST-3-ERROR.+|%GENIE-6-INFO:.+pyATS.+|.%ASYNC_-3-ERROR.+|.%AETEST-4-WARNING.+'
        ShortenListOfText=re.findall(ShortenTextAeTestInfo,f)
        shortenlogpart2=']:.+'

        shortlog=open('resultlog.txt','w+')
        for x in range(len(ShortenListOfText)):
            shortlog.write(ShortenListOfText[x])
            shortlog.write("\n")
        shortlog.close()
        #wrong
        with open('resultlog.txt','r') as log2:
            z=log2.read()
        shortenlistoftextpart2=re.findall(shortenlogpart2,z)
        results=open('newresultlog.txt','w')
        for x in range(len(shortenlistoftextpart2)):
            results.write(shortenlistoftextpart2[x])
            results.write("\n")
        results.close()
        start = ".Caught.error.+|.Caught.an.assertion.+"
        end ="The result of.section.+.FAILED"
        wordx='.The.result.*section (.*) is'
        logfile=open('newresultlog.txt','r')
        line=logfile.read()
        count=0
        blockedcounter=0
        testcasecounter=0
        testcasecounter=0
        if "Starting testcase"in line:
             testcasecounter+=1
        if "is => BLOCKED" in line:
             blockedcounter+=1
        if "result of testcase" in line:
            testcasecounter+=1
                
        if "Caught error" in line:
            count+=1
        if "Caught error while" in line:
            m = re.compile(r'%s.*?%s' % (start,end), re.S)
        
            read=m.search(line).group(0)
            file=open('newnew.txt','w')
            file.write(read)
            list3=re.findall(wordx,read)
            kk=0
            zz=0
            file.close()
            x=0
            with open('newnew.txt','r+') as data_log:
                with open('newnew2.txt','w+')as outfile:
                    for line in data_log:
                        if "Caught error"  in line or "Caught an assertion" in line:
                            print(x)
                            outfile.write("Monster start"+str(kk))
                            outfile.write("\n")
                            kk+=1
                            x+=1
                        if "result of section" in line:
                            pass
                        else:
                            outfile.write(line)
            list=[]
            iter=0
            lineiter=0
            with open('newnew2.txt','r') as finallog:
                if"Monster"+str(iter) in line:
                    list.insert(lineiter,)
                    iter+=1
            filefile=open('newnew2.txt','r')
            ff=filefile.read()
            nana=ff.split('Monster')
            actualfile=open('actually.txt','w')

            print("IFFAFDFDSFSADFDSFASDFDS+++++++++++++++++++++++++++DSFSDFSAF++++++++++++")
                    #print(read)
            while("") in nana:
                nana.remove("")
            for x in range (len(shortversion)):
                actualfile.write(shortversion[x])
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
            #print(shortenlistoftextpart2)
            return shortenlistoftextpart2, nana
