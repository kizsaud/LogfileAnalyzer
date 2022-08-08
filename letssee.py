import re
import json

from tabulate import tabulate
from logfilemake import logmaker
class mate2:
    def line_to_dict(split_Line):
        # Assumes that the first ':' in a line
        # is always the key:value separator

        line_dict = {}
        for part in split_Line:
            key, value = part.split(":", maxsplit=1)
            line_dict[key] = value

        return line_dict
    def bab5():
        word1='result.*testcase (.*) is.+.FAILED'
        word2='The.result.*testcase (.*) is.+.ERRORED'
        word3='The.result.*testcase (.*) is.+.PASSED'
        word4='The.result.*testcase (.*) is.+.ABORTED'
        word5='The.result.*testcase (.*) is.+.SKIPPED'
        word6='The.result.*testcase (.*) is.+.BLOCKED'
        file=open('shortenedlog.txt','r')
        f=file.read()

        shorttext='.Starting testcase.+|.result of.+|.Caught.+|'
        shortentextletssee=re.findall(shorttext,f)

        #write the shortened version to a file, Make this to a method, so it auto does this
        shortlog =open ('shortenedlog222.txt','w+')
        for x in range (len(shortentextletssee)):
            shortlog.write(shortentextletssee[x])
            shortlog.write("\n")
        shortlog.close()
        X=0
        prevline=""
        with open('shortenedlog222.txt','r')as logfile:
            with open('lalaland.txt','w+') as outfile:
                fa=logfile.readlines()
                outfile.write('''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  background: #555;
  background-image: url('https://upload.wikimedia.org/wikipedia/commons/0/08/Cisco_logo_blue_2016.svg');

}

.content {
  max-width: 500px;
  margin: auto;
  background: white;
  padding: 10px;
  
}
p.ex2 {
    text-align: center; 
    font-size: 50px;
    color: green;

}
#boxbutton{
        align-self: center;

     width: 227px;
    height: 50px;
    border-radius: 5px;
    color: green;
}
#testcase{
    color:
}
</style>
</head>
<body>

<div class="content">''')
                
                outfile.write('''<p class="ex2">TESTCASE LOG</p>''')
                outfile.write('''<form>
 <input type="button" id="boxbutton"value="Go back!" onclick="history.go(0)">
</form>''')
                outfile.write('''    <body style="background-color:lightblue;">
''')
                for lines in fa:
                    if 'Starting testcase' in lines:
                        outfile.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        outfile.write("---------------------------------------------------")
                        outfile.write("\n")
                        outfile.write("\n")
                        outfile.write("<b id=testcase>")
                        outfile.write(lines)
                        outfile.write("</b>")
                        outfile.write("\n")
                    if 'result of' in lines:
                        outfile.write("<p>")
                        outfile.write(lines+"|")   
                        outfile.write("</p>")
                        outfile.write("\n")
                        if 'result of testcase' in lines:
                            #outfile.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            outfile.write("\n")
                    if 'Caught' in lines:
                        outfile.write(lines)
                        outfile.write("\n")
                    else:
                        outfile.write(lines)
                outfile.write("<p>+++++++</p>")
                outfile.write("\n")
                outfile.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                prevline=lines
        outfile.close()
        x=0
        failedcase=re.findall(word1,f) 
        #print(failedcase)
        with open('lalaland.txt','r') as hogfile:
            with open('failfile.txt','w') as hotfile:
                for line in hogfile:
                    for x in range(len(failedcase)):
                        if failedcase[x] in line:
                            hotfile.write(line)
                            
        file1=open('lalaland.txt','r')
        ff=file1.read()
        nana=ff.split("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        aka=open('nahbro.txt','w+')
        #print(nana[0])
        z=0
        kk=open('lalaland.txt','r')
        aa=kk.readlines()
        failedsections=[]
        failedsectioniter=0
        for lines in aa:
            if 'Starting testcase' in line:
                pass
            if 'result of section' in lines:
                pass
                if 'FAILED' in lines and 'ERRORED' not in lines:
                    failedsections.insert(failedsectioniter,lines)
                    failedsectioniter+=1
        #print("hi")
        #for x in range(len(failedcase)):
            #print(failedcase[x])
            #print(failedsections[x])
        logfile=open('shortenedlog222.txt','r')
        line=logfile.read()
        start='Starting testcase.+'
        end='result.*testcase (.*) is.+'
        m = re.compile(r'%s.*?%s' % (start,end), re.S)
        read=m.search(line).group(0)


        file=open('wowwoww.txt','w')

        file.write(read)
        file.close()
        counter=0
        with open('wowwoww.txt','r')as logfile222:
            with open('benchod.txt','w') as outfile:
                ka=logfile222.readlines()
                for line in ka:
                    if 'Starting testcase' in line:
                        outfile.write("+++++++++++++++++++++++++++++++++++++++++")
                        outfile.write("\n")
                        outfile.write("\n")
                        if 'result of section' in line:
                            counter+=1
                            outfile.write(counter)
                            outfile.write("\n")
                            outfile.write(lines)
                            outfile.write("\n")
                    
                    else:
                        outfile.write(line)
        benchod=open('benchod.txt','r')
        ff2=benchod.read()
        bobo=ff2.split("+++++++++++++++++++++++++++++++++++++++++")
        while("") in bobo:
            bobo.remove("")
        print(bobo[3])

        testcase=[]
        testcaseiter=0
        resultofsection=[]
        seciter=0
        benchod.close()
        with open('benchod.txt','r') as logfile:
            for line in logfile:
                if "result of testcase" in line:
                    testcase.insert(testcaseiter,line)
                    testcaseiter+=1
                if 'result of section' in line:
                    if 'FAILED' or 'ERRORED' or 'BLOCKED' or 'SKIPPED' in line:
                        resultofsection.insert(seciter,line.strip('\n'))
        splitcontent=ff2.split("+++++++++++++++++++++++++++++++++++++++++")
        #print(testcase)
        print(resultofsection)
        
        
        from unittest import result



        prevline=''
        with open('regularlog.txt','r+')as logfile:
            with open ('regularlog2.txt','w') as resultfile:
                f=logfile.readlines()
                resultfile.write('''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  background: #555;
  background-image: url('https://upload.wikimedia.org/wikipedia/commons/0/08/Cisco_logo_blue_2016.svg');

}

.content {
  max-width: 1500px;
  margin: auto;
  background: white;
  padding: 10px;
  
}
p.ex2 {
    text-align: center; 
    font-size: 50px;
    color: green;

}
#boxbutton{
        align-self: center;

     width: 227px;
    height: 50px;
    border-radius: 5px;
    color: green;
}
#testcase{
    color:
}
</style>
</head>
<body>

<div class="content">''')
                resultfile.write('''<script>
function myFunction() {
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}
</script>''')
                resultfile.write('''<p class="ex2">TESTCASE LOG</p>''')
                resultfile.write(''''<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for names.." title="Type in a name">''')
                resultfile.write('''<body style="background-color:lightblue;"''')
                resultfile.write('''<form>
 <input type="button" id="boxbutton"value="Go back!" onclick="history.go(0)">
</form>''')
                resultfile.write('''<ul id="myUL">''')
                for line in f:
                    if 'Starting testcase' in line:
                        resultfile.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        resultfile.write("\n")
                    if 'result of testcase' in line:
                        resultfile.write("<b>")
                        resultfile.write(line)
                        resultfile.write("</b>")
                        resultfile.write("-XASEWASDASDFASDFASDFASDKLFASDKFLASDFASDLFKADSFDSAFKDSFASDKFASDFKASDFASDKFASD--XASEWASDASDFASDFASDFASDKLFASDKFLASDFASDLFKADSFDSAFKDSFASDKFASDFKASDFASDKFASD-")
                        resultfile.write("\n")
                        resultfile.write("\n")
                    if '+------------------------------------------------------------------------------+' in line:
                        pass
                    else:
                        resultfile.write('''<li><a href="#">''')
                        resultfile.write(line)
                        resultfile.write("</a></li>")
                prevline=line
            
        nope=open('regularlog2.txt','r')
        zz=nope.read()
        kaka=zz.split("-XASEWASDASDFASDFASDFASDKLFASDKFLASDFASDLFKADSFDSAFKDSFASDKFASDFKASDFASDKFASD--XASEWASDASDFASDFASDFASDKLFASDKFLASDFASDLFKADSFDSAFKDSFASDKFASDFKASDFASDKFASD-")

        return kaka