import sqlite3
from flask import Flask,render_template,request
import random
import json
import os.path
import subprocess

app = Flask(__name__)

@app.route("/")
def main(): 
    return render_template("site.html")


@app.route("/input")
def get_input():
    db= sql.connect("database.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM input")
    rows = cur.fetchall()
    cur.close()
    db.close()
    return json.dumps(rows)


@app.route("/add_input",methods=["POST"])
def add_input():
    
    confirmation = random.randint(0, 100)

    an1 = request.form["an1"]
    c = request.form["c"]
    an2 = request.form["an2"]
    x = request.form["x"]
    an3 = request.form["an3"]
    d = request.form["d"]
    an4 = request.form["an4"]
    y = request.form["y"]
    n = request.form["n"]
    a0 = request.form["a0"]
    a1 = request.form["a1"]

    db=sqlite3.connect("database.db")
    cur = db.cursor()
    cur.execute("INSERT INTO input(confirmation,an1,c,an2,x,an3,d,an4,y,a0,a1,n) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(confirmation,an1,c,an2,x,an3,d,an4,y,a0,a1,n))
    db.commit()

    cur.close()
    db.close()
    
    print("computing")
    subprocess.run("python3 'demon.py'", shell = True)
    
    return "Your input has been submitted! Your confirmation number will be used to view your results once they are complete. Your confirmation number is: " + str(confirmation) 


@app.route("/results", methods=["POST"])
def results():

    confirmation1 = request.form["confirmation"]

    file_name = confirmation1 + "_results.txt"

    if os.path.isfile(file_name) == True:
        return("Use this link to view your results: cs.longwood.edu/~blackstonecb/cmsc490/" +file_name )
        #return render_template("confirmation.html")
    else:
        return "Results are not ready yet. Please try again later"

app.run(host="0.0.0.0", port=6001)
