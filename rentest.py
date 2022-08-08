    
from cgi import test
from unittest import TestCase
def reasongrabber():
    filename='RENN_test_job_1721_2.report'
    testcases=['Tsz7693096c','Tsz7693111c','Tsz7693114c','Tsz7693115c']
    failed=[]
    failediter=0
    errored=[]
    errorediter=0
    x=0
    steplist=[]
    steplistiter=0
    abortlist=[]
    abortiter=0
    skipped=[]
    skippediter=0
    with open(filename) as f:
        for line in f:
            
            if "Task Result Details "in line:
                nextline=next(f)
            if "PASSED" in line:
                print(line)
            if "ERRORED" in line and "Task-1" not in line and "STEP" not in line:
                errored.insert(errorediter,line.strip('ERRORED\n'))
                errorediter+=1
            if "FAILED" in line:
                failed.insert(failediter,line.strip('FAILED\n'))
                failediter+=1
            if "ABORTED" in line:
                abortlist.insert(abortiter,line.strip('ABORTED\n'))
                abortiter+=1
            if "SKIPPED" in line:
                skipped.insert(skippediter,line.strip('SKIPPED\n'))
                skippediter+=1
                
    print(errored)
    y=0
    z=0

   
    while(testcases[y]) not in errored[z]:
        y+=1
        if testcases[y] in errored[z]:
            errored.remove(errored[z])
            y+=1
   
           

    print("Change")
    print(errored)
        
        
    
reasongrabber()