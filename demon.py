import sqlite3
import time
import subprocess 
import random

def main():

    db = sqlite3.connect("database.db")
    cur = db.cursor()
    cur.execute("SELECT COUNT(*) FROM input")
    result = cur.fetchone()

    rows = result[0]

    if rows >= 1:
        print("Yes, there is input in the table")
        print("The number of rows is: " + str(rows))
        write()
    else:
        print("no, there is not input in the table")
        print("The number of rows is : " + str(rows))
   

def write():

    db = sqlite3.connect("database.db")
    cur = db.cursor()
    f = open("inputs.txt", "w")
    cur.execute("SELECT * FROM input") 
    inputs = cur.fetchone()
    #
    #confirmation
    f.write(inputs[0])
    f.write("\n")

    #an1
    f.write(inputs[1]) 
    f.write("\n")
    #c
    f.write(inputs[2]) 
    f.write("\n")
    #an2
    f.write(inputs[3]) 
    f.write("\n")
    #x
    f.write(inputs[4]) 
    f.write("\n")
    #an3
    f.write(inputs[5]) 
    f.write("\n")
    #d
    f.write(inputs[6]) 
    f.write("\n")
    #an4
    f.write(inputs[7]) 
    f.write("\n")
    #y
    f.write(inputs[8]) 
    f.write("\n")
    #a0
    f.write(inputs[9]) 
    f.write("\n")
    #a1
    f.write(inputs[10]) 
    f.write("\n")
    #n
    f.write(inputs[11]) 
    f.write("\n")

    f.close()
    
    cur.execute("SELECT COUNT(*) FROM input")
    result = cur.fetchone()
    rows = result[0]
    
    if rows == 0:
        print("no more code to process")
       # cur.close()
       # db.close()
    else:
        cur.execute( "DELETE FROM input WHERE confirmation=?", [inputs[0]])
        db.commit()
        print("The delete command has been executed")

    cur.close()
    db.close()
    
    print("launching a process..")
    completed = subprocess.run("./a.out 'main.cpp'", shell = True)
    print("Process completed the code")
    check()

def check():
    db = sqlite3.connect("database.db")
    cur = db.cursor()
    old_count= cur.execute("SELECT * FROM input")
    
    time.sleep(5)
  
    new_count = cur.execute("SELECT * FROM input")
    print("checking..")
    print(new_count)
    main()

if __name__ == "__main__":
    main()
