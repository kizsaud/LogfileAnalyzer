ind=1
ind2=1
line2=[]
txt2='.Starting testcase.'
txt='.Starting.'
testcase=[]
result=[]
table ={}
Section=[]
sectionresult=[]
failedreason=[]
skippedreason=[]
testcaseerrorreason=[]
Sectionblockedreason=[]
sectionfailedreason=[]
erroredreason=[]
blockedreason=[]
abortreason=[]
failedsections=[]
ind=0
ind2=0
ind3=0
skipind=0
erroriter=0
blockiter=0
prevline=""
abortiter=0
findex=0
testcaseerrorindex=0
secretfailedreasons=[]
secindex=0
post=[]
errorsection=[]
postpreind=0
pre=[]
preind=0
abortrare=[]
abortrareiter=0
blockedlist=[]
blocediter=0
blockedreason=[]
blockedreasoniter=0
sectionfailedreasonreason=[]
sectionfailedreasonreasoniteriter=0
class preprint:
    def jack():
    
        with open('new.txt','r') as log3:
            for line in log3:
                if "subsection" in line:
                    if "ABORTED" in line:
                        abortrare.insert(0,line)
                        
                if "Starting testcase" in line:
                    testcase.insert(ind,line.strip('\n'))
                    ind+=1
                    
                if "Failed reason" in line:
                    secretfailedreasons.insert(secindex,line)
                    secindex+=1
                        
                if "The result of section" in line:
                    Section.insert(ind,line)
                    ind+=1
                    
                    if "FAILED" in line:
                        failedsections.insert(findex,line)
                        if "reason" in prevline:
                            sectionfailedreason.insert(ind2,prevline)
                        else:
                            sectionfailedreasonreason.insert(sectionfailedreasonreasoniteriter,"no fail reason found\n")
                        ind2+=1
                        findex+=1
                        sectionfailedreasonreasoniteriter+=1
                        print(prevline)
                    if "ERRORED" in line:
                        errorsection.insert(erroriter,line)
                        erroredreason.insert(erroriter,prevline.strip('pyATS Health Check get_devices '))
                        erroriter+=1
                        print(prevline)
                    if "BLOCKED" in line and "reason" in prevline:
                        blockedreason.insert(blockiter,prevline)
                        
                    
                if 'The result of Post'  in line:
                    if "FAILED" in line:
                        
                        post.insert(postpreind,line)
                        postpreind+=1
                if 'The result of Pre'in line:
                    if "FAILED" in line:
                        pre.insert(preind,line)
                        preind+=1   
                if "result of testcase" in line:
                    result.insert(ind3,line)
                    ind3+=1
                    if "BLOCKED" in line:
                        blockedlist.insert(blocediter,line)
                        blocediter+=1
                        if "Blocking" in prevline:
                            blockedreason.insert(blockedreasoniter,prevline)
                            blockedreasoniter+=1
                            
                        
                    if "SKIPPED" in line:
                        skippedreason.insert(skipind,prevline)    
                        skipind+=1
                    if "ERRORED" in line and "reason" in prevline:
                        erororor=0
                        for x in range(len(testcase)):
                            Section[x]
                            if "ERRORED" in Section[x]:
                                testcaseerrorreason.insert(testcaseerrorindex,Section[x])
                            else:
                                break
                        ti=0
                        if "PASSED" not in prevline:
                            testcaseerrorreason.insert(erororor,prevline)
                        else:
                            for x in range (len(erroredreason)):
                                testcaseerrorreason.insert(ti,erroredreason[x])
                                ti+=1

                    if "ABORTED" in line:
                        for x in range(len(Section)):
                            Section[x]
                            if "ABORTED" in Section[x]:
                                abortreason.insert(abortiter,"ABORTED DUE TO:" + Section[x])
                        
                    #if "FAILED" in line:
                    #   skippedreason.insert()
                prevline=line
printer2.setup(testcase,result,skippedreason,testcaseerrorreason,Section,sectionfailedreason,erroredreason,blockedreason,abortreason,failedsections,pre,post,errorsection,abortrare,blockedlist,blockedreason,sectionfailedreasonreason,secretfailedreasons)
