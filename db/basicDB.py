#DB entry through input file and extract data to output file

import sqlite3

conn = sqlite3.connect("miniProject.db")
c= conn.cursor()

createTablecmd = open("inputCreateTable.txt","r").read() #ioClass to str
studentNames =open("studentNames.txt","r").read()
studentRollNos = open("studentRolls.txt","r").read()


def createTable():
    c.execute(createTablecmd)


def dynamicEntry():
    c.execute("INSERT INTO student(name,rollnumber) VALUES(?,?)",(studentNames,studentRollNos))
    conn.commit()


def selectFromDB():
    outputcmd=open("findOutScript.txt","r").read()
    output =c.execute(outputcmd)
    print("type of output",type(output))
    data = output.fetchall()
    print("type of data is ", type(data),"data is : ",data)
    


createTable()
dynamicEntry()
selectFromDB()