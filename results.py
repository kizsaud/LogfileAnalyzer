import re
import fileinput
from tabulate import tabulate

class loglinkdata:
    def loglinkdatamethod():
        start = ".Starting testcase.+"
        end =".The result of testcase.+"
        wordx='The.result.*testcase (.*) is'
        count=0
        blockedcounter=0
        testcasecounter=0
        testcasecounter=0
        logfile=open('new.txt','r')
        line=logfile.read()
        if "Starting testcase"in line:
                testcasecounter+=1
        if "is => BLOCKED" in line:
            blockedcounter+=1
        if "result of testcase" in line:
            testcasecounter+=1
                
        if "Caught an exception" in line and "Errored reason" not in line:
            count+=1
        if count>0 and blockedcounter != testcasecounter and testcasecounter!=0:
            m = re.compile(r'%s.*?%s' % (start,end), re.S)

            
            m = re.compile(r'%s.*?%s' % (start,end), re.S)
            read=m.search(line).group(0)
            #print(read)
            file=open('data.txt','w')
            file.write(read)    
            list2=re.findall('The.result.of.testcase.+',read)
            list3=re.findall(wordx,read)
            print(list3)
            #print(list2)
            x=0
            kk=0
            zz=0
            with open('data.txt','r+') as data_log:
                with open('data2.txt','w+') as outfile:
                    for line in data_log:
                        if "Starting testcase" in line:
                            outfile.write("Monster Start:" +str(kk))
                            outfile.write("\n")
                            
                            outfile.write("\n")
                            kk+=1
                        if "The result of testcase" in line:
                            outfile.write(line)

                            outfile.write("Monster end:"+ " " + str(zz))
                            outfile.write("\n")
                            zz+=1
                        else:
                            outfile.write(line)
            list=[]
            iter=0
            lineiter=0
            with open('data2.txt','r') as finallog:
                with open('section.txt','w') as openlog:
                    for line in finallog:
                        if "Monster:"+str(iter) in line:
                            list.insert(lineiter,)
                            print("success")
                            iter+=1
            filefile=open('data2.txt','r')
            ff=filefile.read()
            nana=ff.split('Monster Start:')
            #print(nana[1])
            while("" in nana) :
                nana.remove("")

            keys=range(len(list3))
            value=nana
            dict={}
            print("+++++++++++++++++++++++++++++++++")
       
            return nana
class monsterdata:
    def dictmaker():
        dictttt={}
        dictttt=loglinkdata.loglinkdatamethod()
        file=tabulate(dictttt[0],tablefmt='html',showindex=True)
        file2=open('monster.txt','w')
        file2.write(file)
        return dictttt