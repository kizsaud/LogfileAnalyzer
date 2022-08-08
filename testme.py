from flask import Flask, render_template 
from tablebaber import tablebabmaker
app=Flask(__name__)

biglist=[]
biglist=tablebabmaker.tablemaker()
Names=[]
names=biglist[0]
Pass_FAIL=[]
Pass_FAIL=biglist[1]
Result_LIST=[]
Result_LIST=biglist[2]
detailed_REASON=[]
detailed_REASON=biglist[3]
LOGLINK=[]
LOGLINK=biglist[4]

@app.route("/")
def table():
    return render_template("table.html",Names=Names,Pass_FAIL=Pass_FAIL,Result_LIST=Result_LIST,detailed_REASON=detailed_REASON)