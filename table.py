import pandas as pd
import webbrowser


from tabulate import tabulate
import re
from shortlogana import bb2
from testfailed import LibraryGrabber
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
class tablemaker:
    def tablemaker():
        #dictoflogs={}
        #dictoflogs=loglinkdata.loglinkdatamethod()
        #pd=pd.read_csv('results.txt',sep="the result of testcase", header=None)
        #table=print(tabulate(pd,tablefmt='pretty'),end=' ')
        with open('results.txt','r') as log:
            f=log.read() 
        word='The.result.*testcase (.*) is'
        word2='testcase.*=> (FAILED|PASSED|ERRORED|BLOCKED|ABORTED|SKIPPED)'
        word3='.*ERRORED FROM:(.*)|Testcase was skipped|Abort reason:(.*)|Preason:(.*)|ABORTED DUE TO:]:(.*)|UKNOWN SECTION:|FAIL DUE TO:]:(.*)|Errored-w reason:(.*)|Block reason:(.*)'
        word4='.*ERRORED REASON:(.*)|Fail reason:(.*)|ERRORED REASON:(.*)|Skipped reason:(.*)|Errored reason:(.*)|Preason:(.*)|Failed reason:(.*)'
        abortword='Caught.+.aborting.+'
        list2=re.findall(word,f)
        list3=re.findall(word2,f)
        list4=re.findall(word3,f)
        list5=re.findall(word4,f)
        list6=re.findall(abortword,f)
        #list7=bb2.hater()
        list8=LibraryGrabber.LibraryGrab()
        list9=[]
        #if list8:
         # list9=list7+list8
        #if list7 and list8:
         # list9=list7+list8
               
        #print(list2)
        #print(len(list2))
        #print(list4)
        print(len(f))
        table = [[list2],[list3],[list4]]

        if list8:
              dict = {"TESTCASE:":list2,"PASSED/FAILLED":list3,"REASON":list8}
              dict2={"TESTCASE:":list2,"PASSED/FAILLED":list3,"From":list4,"Possible reason:":list5,"ERRORED REASONS":list8}
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
    
tablemaker.tablemaker()