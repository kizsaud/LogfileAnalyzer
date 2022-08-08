import pandas as pd
import webbrowser


from tabulate import tabulate
import re
from shortlogana import bb2
from testfailed import LibraryGrabber
from shortlogana2 import bb3
global big
big='''<!DOCTYPE html>
<html>
  <head>
    <title>Flask app</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
  </head>
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pass Python variable to Javascript</title>
</head>
<body>


 <script>   
  var selectvalue = document.getElementById("selectvalue"), test = {{ name | tojson }};
function displayvar(){
    for(var i = 0; i<test.length; i++)
    console.log(test[i])
    console.log('%cEND TESTCASE', 'color: red; font-size: 30px;');
 
}
</script>
<button class="displayvar" onclick="displayvar();">Display log on console</button>



</body>
</html>
 '''
class tablebabmaker:
    def tablemaker():
        #dictoflogs={}
        #dictoflogs=loglinkdata.loglinkdatamethod()
        #pd=pd.read_csv('results.txt',sep="the result of testcase", header=None)
        #table=print(tabulate(pd,tablefmt='pretty'),end=' ')
        with open('results.txt','r') as log:
            f=log.read() 
        #testCASE
        word1='The.result.*testcase (.*) is.+.FAILED'
        word2='The.result.*testcase (.*) is.+.ERRORED'
        word3='The.result.*testcase (.*) is.+.PASSED'
        word4='The.result.*testcase (.*) is.+.ABORTED'
        word5='The.result.*testcase (.*) is.+.SKIPPED'
        word6='The.result.*testcase (.*) is.+.BLOCKED'
        #++++++++++++++++++++++++++++++++++++++++++++++++++TESTCASENAME

        #PASS/FAIL/ABORT
        word12='testcase.*=>.(FAILED)'
        word21='testcase.*=>.(ERRORED)'
        word31='testcase.*=>.(PASSED)'
        word41='testcase.*=>.(ABORTED)'
        word51='testcase.*=>.(SKIPPED)'
        word61='testcase.*=>.(BLOCKED)'
        #+++++++++++++++++++++++++++++++++++++++++++++++++++RESULT
        
       
              
        #Failed From
        word13='FAIL DUE TO:.:.(.*)'
        #ERRORED FROM
        ERRORED_FROM='ERRORED FROM:..(.*)'
        #PASS FROM
        PASS_FROM='Preason:(.*)'
        #ABORTED FROM
        ABORT_FROM='THIS testcase was aborted, we found the section for the aborting:.(.*)'
        #SKIPPED FROM
        SKIPPED_FROM='Testcase was(.*)'
        #++++++++++++++++++++++++++++++++++++++++++++++++++POST/PRE/SECTION
        testFailedAnalysis_reason=[]
        TestErrorAnalysis_reason=[]
        
        #FAILED REASON
        if LibraryGrabber.LibraryGrab() != None:
            testFailedAnalysis_reason=LibraryGrabber.LibraryGrab()
            while("")in testFailedAnalysis_reason:
                testFailedAnalysis_reason.remove("")
        else:
              failedtext='Failed.reason(.*)'
              testFailedAnalysis_reason=re.findall(failedtext,f)
        #ERRORED REASON
        if bb2.hater() != None:
              TestErrorAnalysis_reason=bb2.hater()
              while("") in TestErrorAnalysis_reason:
                    TestErrorAnalysis_reason.remove("")
        #PASSED TAKEN CARE OF BELOW!
        
      #ABORT NEEDE
      #SKIP NEEDED
      #BLOCKED
        BLOCKEDTEXT='Block.reason:(.*)'
        BLOCKTEXTERROR=re.findall(BLOCKEDTEXT,f)
        print("+++++++++++++++++++++++++here")
        print(BLOCKTEXTERROR)
        #reason list
        
        
        
        #word4='.*ERRORED REASON:(.*)|Fail reason:(.*)|ERRORED REASON:(.*)|Skipped reason:(.*)|Errored reason:(.*)|Preason:(.*)|Failed reason:(.*)'
        #abortword='Caught.+.aborting.+'
        ########################
        #TESTCASE NAMES FAILED ERRORED PASSED ABORTED SKIPPED BLOCKED
        list2=re.findall(word1,f)
        list3=re.findall(word2,f)
        list4=re.findall(word3,f)
        list5=re.findall(word4,f)
        list6=re.findall(word5,f)
        list7=re.findall(word6,f)
        list8=list2+list3+list4+list6+list7
        #+++++++++++++++++++++++++++
        #FAILED/ERRORED/PASSED/ABORTED/SKIPPED (RESULT!)
        PFA_LIST1=re.findall(word12,f)
        PFA_LIST2=re.findall(word21,f)
        PFA_LIST3=re.findall(word31,f)
        PFA_LIST4=re.findall(word41,f)
        PFA_LIST5=re.findall(word51,f)
        PFA_LIST6=re.findall(word61,f)
        PFA_LIST_TOTALS=PFA_LIST1+PFA_LIST2+PFA_LIST3+PFA_LIST4+PFA_LIST5+PFA_LIST6
        #Grab the length of passed testcases
        PASSED_LIST_LENGTH=[]
        PASSED_LIST_ITER=0
        #Create a list with elements "None" the size of how many passed testcases there is
        
        for x in range(len(PFA_LIST3)):
              PASSED_LIST_LENGTH.insert(x,"none")
        
        #CREATE A REASON LIST, ORDER: FAILED.errored.PASSED.ABORTED.SKIPPED BLOCKED 
        #CURRENT SITUATION FAILED+ERROR+PASS, NEED ABORT AND SKIP!   
        reasonlist=testFailedAnalysis_reason+TestErrorAnalysis_reason+PASSED_LIST_LENGTH+BLOCKTEXTERROR
      
        #+++++++++++++++++++++++++++++++++
        #Fail due to!(SECTION/POST/PRE)
        FAIL_DUE_TO=re.findall(word13,f)
        #ERROR DUE TO!
        ERRORED_FROM_FINDER=re.findall(ERRORED_FROM,f)
        #PASS DUE TO
        PASSED_FROM_FINDER=re.findall(PASS_FROM,f)
        #ABORTED
        ABORT_FROM_FINDER=re.findall(ABORT_FROM,f)
        #SKIPPED
        SKIPPED_FROM_FINDER=re.findall(SKIPPED_FROM,f)
        #ADD ALL 
        FINDER_LIST=FAIL_DUE_TO+ERRORED_FROM_FINDER+PASSED_FROM_FINDER+ABORT_FROM_FINDER+SKIPPED_FROM_FINDER+BLOCKTEXTERROR
        #++++++++++++++++++++++++++++++++++++++++++++++++++
        #REASON, IF ANY!
        print("++++++++++")
        #print(testFailedAnalysis_reason[0])
        #print(TestErrorAnalysis_reason[0])
        #Create a dictionary for second table, while will contain the detailed reasons of failure.
        new={}
        REASONLISTWITHOUTPASSED=testFailedAnalysis_reason+TestErrorAnalysis_reason+BLOCKTEXTERROR
        LISTWITHOUTPASS=list2+list3+list5+list6+list7
        NOPASSEDRESULTFINDER_LIST=FAIL_DUE_TO+ERRORED_FROM_FINDER+ABORT_FROM_FINDER+SKIPPED_FROM_FINDER+BLOCKTEXTERROR
        #print(tabulate(new,tablefmt='psql',headers=["Testcase","reason"],showindex=True))
        #df=pd.DataFrame(REASONLISTWITHOUTPASSED,index=LISTWITHOUTPASS)
        fiel=open('momma.html','w')
        #print(df)
        failedf=bb3.hater()
        dict2={"TESTCASE:":list8,"PASSED/FAILLED":PFA_LIST_TOTALS,"Section":NOPASSEDRESULTFINDER_LIST,"reason":failedf}
        word='''<div class="split left">
  <div class="centered">
  <div>

'''     
        word2='''  </div>

'''     
        word3='''<div class="split right">
  <div class="centered">
  <div>
  
   '''
        word4='''   </div>
  '''
  
        word5='''<!DOCTYPE html>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial;
            color: white;
        }
        
        .split {
            height: 100%;
            width: 50%;
            position: fixed;
            z-index: 1;
            top: 0;
            overflow-x: hidden;
            padding-top: 20px;
        }
        
        .left {
            left: 0;
            background-color: #111;
            overflow: scroll;
        }
        
        .right {
            right: 0;
            background-color: red;
            transform: translate(0%, -2%);
            overflow: scroll;
        }
        
        .centered {
            position: absolute;
            text-align: center;
        }
    </style>
</head>

<body>

    <div class="split left">
        <div class="centered">'''
        wrd6='''</div>'''
        wrd7='''<div class="split right">
        <div class="centered">

'''
        wrd8='''</body>

</html>'''
        fiel.write(word5)
        fiel.write(tabulate(dict2,tablefmt='html',headers=["TESTCASE","Result","From:"],showindex=True))
        fiel.write(wrd6)
        #fiel.write(word2)
        #fiel.write(word5)
        #fiel.write("<center>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++DETAILED REASONS OF FAILURE++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++</center>")
        #fiel.write(word3)
        fiel.write(wrd7)
        fiel.write(tabulate(dict2,headers='keys',tablefmt='html'))
        fiel.write(wrd6)
        fiel.write(wrd8)


        if list8:
              dict = {"TESTCASE:":list8,"PASSED/FAILLED":PFA_LIST_TOTALS,"REASON":FINDER_LIST}
              dict2={"TESTCASE:":list8,"PASSED/FAILLED":PFA_LIST_TOTALS,"From":FINDER_LIST,"Reason, if any:":reasonlist}
              f=open('result.html','w')
              f.write(tabulate(dict2,tablefmt='html',headers=["TESTCASE","Result","From:","Reason, if any","errored reason in order, if any"],showindex=True))
              f.write(big)
              print(tabulate(dict,tablefmt='pretty',headers=["TESTCASE#","TESTCASE NAME:","RESULT","FAIL DUE TO:","FAILURE REASON IF"],showindex=True))
        else:
              dict = {"TESTCASE:":list2,"PASSED/FAILLED":list3,"REASON":list4}
              dict2={"TESTCASE:":list2,"PASSED/FAILLED":list3,"From":list4,"Possible reason:":list5}
              f=open('result.html','w')
              f.write(tabulate(dict2,tablefmt='html',headers=["TESTCASE","Result","From:","Reason, if any"],showindex=True))
              f.write(big)


                  
        
        
        f.close()
        print(list4)
    
tablebabmaker.tablemaker()