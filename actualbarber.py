import pandas as pd
import webbrowser


from tabulate import tabulate
import re
from shortlogana import bb2
from testfailed import LibraryGrabber
from shortlogana2 import bb3
from testfailed import LibraryGrabber
from helpdde import getme
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
    def tablemaker(nameofjob,versiongit):
        versiongit=open('versiongit.txt','r')
        fa234=versiongit.readlines()
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
        check=open('results.txt','r')
        checklog=check.read()
       
              
        #Failed From
        word13='FAIL.DUE.TO:.:.The.result.of.(.*)is.=>.FAILED'
        #ERRORED FROM
        ERRORED_FROM='ERRORED FROM:.:.The result of section(.*).is.+.ERRORED'
        #PASS FROM
        PASS_FROM='Preason:(.*)'
        #ABORTED FROM
        ABORT_FROM='THIS testcase was aborted, we found the section for the aborting:.(.*)'
        #SKIPPED FROM
        SKIPPED_FROM='Testcase was(.*)'
        #++++++++++++++++++++++++++++++++++++++++++++++++++POST/PRE/SECTION
        testFailedAnalysis_reason=[]
        TestErrorAnalysis_reason=[]
        TestErrorAnalysis_reason
        skippedreason=[]
        failmetoo=[]
        actualfailreason=[]
        actualallreason=[]

        if bb2.hater()!=None:
            x,actualfailreason=bb2.hater()
        else:
            pass
        if LibraryGrabber.LibraryGrab()!=None:
            x,failmetoo=LibraryGrabber.LibraryGrab()
        else:
            pass
        actualallreason=[]
        if failmetoo:
            actualallreason+=failmetoo
        if actualfailreason:
            actualallreason+=actualfailreason

        #if actualerrored:
        #    actualallreason+=actualerrored
        #FAILED REASON
        if LibraryGrabber.LibraryGrab() != None:
            testFailedAnalysis_reason,failmetoo=LibraryGrabber.LibraryGrab()
            while("")in testFailedAnalysis_reason:
                testFailedAnalysis_reason.remove("")
        else:
              failedtext='Failed.reason:(.*)'
              testFailedAnalysis_reason=re.findall(failedtext,f)
        #ERRORED REASON
        if bb2.hater() != None:
            TestErrorAnalysis_reason,x=bb2.hater()
            while("") in TestErrorAnalysis_reason:
                    TestErrorAnalysis_reason.remove("")
        else:
            erroredtext='ERRORED.REASON:.:.Errored.reason:+.(.*)'
            TestErrorAnalysis_reason=re.findall(erroredtext,f)
            if TestErrorAnalysis_reason ==None:
                erroredtext='ERRORED.REASON..:.(.*)'
                TestErrorAnalysis_reason=re.findall(erroredtext,f)
        #PASSED TAKEN CARE OF BELOW!
        if "Skipped reason" in checklog:
            
            skippedreason='Skipped reason:(.*)'
            SkippedAnalysis=re.findall(skippedreason,f)
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
        reasonlist=[]
        if testFailedAnalysis_reason:
            reasonlist+=testFailedAnalysis_reason
        if TestErrorAnalysis_reason:
            reasonlist+=TestErrorAnalysis_reason
        if skippedreason:
            reasonlist+=SkippedAnalysis
        if BLOCKTEXTERROR:
            reasonlist+=BLOCKTEXTERROR
        
            
      
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
        REASONLISTWITHOUTPASSED=testFailedAnalysis_reason
        LISTWITHOUTPASS=list2+list3+list5+list6+list7
        NOPASSEDRESULTFINDER_LIST=FAIL_DUE_TO+ERRORED_FROM_FINDER+ABORT_FROM_FINDER+SKIPPED_FROM_FINDER+BLOCKTEXTERROR
        #print(tabulate(new,tablefmt='psql',headers=["Testcase","reason"],showindex=True))
        #df=pd.DataFrame(range(len(list8)),index=reasonlist)
        dict1={"Testcase:":LISTWITHOUTPASS,"Error reason:":reasonlist}
        fiel=open('momma.html','w')
        print(len(list8))
        #print(len(reasonlist))
        detailed_reason=[]
        Log_link=[]
        Analysis=[]
        popup="Link"
        popup2="SCRIPT/image"
        Actual_fail=bb3.hater()
        if Actual_fail:
            pass
        else:
            Actual_fail+=testFailedAnalysis_reason
        
        for x in range (len(LISTWITHOUTPASS)):
            detailed_reason.insert(x,popup)
        for x in range(len(LISTWITHOUTPASS)):
            Log_link.insert(x,popup)
        AnalysisImageScript=[]    
        AISITER=0
        for x in range(len(reasonlist)):
            if "Python" in reasonlist[x]:
                AnalysisImageScript.insert(AISITER,"Script issue")
                AISITER+=1
            if 'unexpected return code' or 'gnoi' in reasonlist[x]:
                AnalysisImageScript.insert(AISITER,"Script issue")
                AISITER+=1
           
            else:
                AnalysisImageScript.insert(AISITER,"Image issue")
                AISITER+=1
        dict2={"TESTCASE:":list8,"PASSED/FAILLED":PFA_LIST_TOTALS,"Section":NOPASSEDRESULTFINDER_LIST,"Analysis":reasonlist,"IMAGESCRIPT":AnalysisImageScript}
        data='''<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
'''     

        data5='''  <body>


 <script>   
  var selectvalue = document.getElementById("selectvalue"), test = {{ name | tojson }};
  var selectvalue2=document.getElementById("selectvalue"), test2 = {{ allresults | tojson }};;
  
function displayvar(){
    var result = prompt('type which testcase number youd like to see');

    alert(test[result])
 
}
function displayvar2(){
    var result = prompt('type up to which testcase youd like to see');

    alert(test2[result])
  

}
 
</script>
<script type="text/javascript">
        $(document).ready(function () {

$("#flip").click(function () {
            $("#panel").slideToggle("slow");
        });

        $("#flip1").click(function () {
            $("#panel1").slideToggle("slow");
        });

           //Filter table
      var $rows = $('#table tr');
$('#search').keyup(function() {
    
    var val = '^(?=.*\\b' + $.trim($(this).val()).split(/\s+/).join('\\b)(?=.*\\b') + ').*$',
        reg = RegExp(val, 'i'),
        text;
    
    $rows.show().filter(function() {
        text = $(this).text().replace(/\s+/g, ' ');
        return !reg.test(text);
    }).hide();
});

            
 });
</script>
<button class="displayvar" onclick="displayvar();"> Detailed reason</button>
<button class="displayvar2" onclick="displayvar2();"> Testcase log </button>



</body>
<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
        
'''     
        headerstyle='''<!DOCTYPE html>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * {
            box-sizing: border-box;
        }
        
        #myInput {
            background-image: url('/css/searchicon.png');
            background-position: 10px 10px;
            background-repeat: no-repeat;
            width: 100%;
            font-size: 16px;
            padding: 12px 20px 12px 40px;
            border: 1px solid #ddd;
            margin-bottom: 12px;
        }
        
        #myTable {
            border-collapse: collapse;
            width: 100%;
            border: 1px solid #ddd;
            font-size: 18px;
        }
        
        #myTable th,
        #myTable td {
            text-align: left;
            padding: 12px;
        }
        
        #myTable tr {
            border-bottom: 1px solid #ddd;
        }
        
        #myTable tr.header,
        #myTable tr:hover {
            background-color: #f1f1f1;
        }
    </style>
   '''
     

        if dict2:
            fiel.write(data)
            fiel.write(data5)
            
            fiel.write(headerstyle)
            fiel.write('''    <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for names.." title="Type in a name">
''')    
            fiel.write(tabulate(dict2,tablefmt='html',headers=["S.No","Testcase","Result:","SECTION","Reason","Analysis"],showindex=True))
            
           
           
        #fiel.write(wrd6)
        #fiel.write(word2)
        #fiel.write(word5)
        #fiel.write("<center>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++DETAILED REASONS OF FAILURE++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++</center>")
        #fiel.write(word3)
        #fiel.write(wrd7)
        #fiel.write(wrd9)
        #if dict1:
         #   fiel.write(tabulate(dict1,headers='keys',tablefmt='html'))
        #fiel.write(wrd6)
        #fiel.write(wrd8)


    
                  
        # Read in the file
        with open('momma.html', 'r') as file :
            filedata = file.read()

# Replace the target string
        filedata = filedata.replace('<table>', '<table id="myTable">')

# Write the file out again
        with open('momma.html', 'w') as file:
            file.write(filedata)
            file.write(  '''<script>
   function myFunction() {
            var input, filter, table, tr, td, i, txtValue;
            input = document.getElementById("myInput");
            filter = input.value.toUpperCase();
            table = document.getElementById("myTable");
            tr = table.getElementsByTagName("tr");
            for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[2];
                if (td) {
                    txtValue = td.textContent || td.innerText;
                    if (txtValue.toUpperCase().indexOf(filter) > -1) {
                        tr[i].style.display = "";
                    } else {
                        tr[i].style.display = "none";
                    }
                }
            }
        }
</script>''')
        
        fiel.close()
        #print(list4)
        print("HERE!##")
        print(TestErrorAnalysis_reason)
        return actualallreason
