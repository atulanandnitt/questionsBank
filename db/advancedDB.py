
import sqlite3

conn = sqlite3.connect("miniProject.db")
c= conn.cursor()

"""
with open("studentNames.txt","r") as studentFile:
    studentNames = studentFile.read()
    
"""    
createTablecmd = open("inputCreateTable.txt","r").read() #ioClass to str
studentNames =open("studentNames.txt","r").read()
studentRollNos = open("studentRolls.txt","r").read()


def createTable():
    c.execute(createTablecmd)


def dynamicEntry():
    c.execute("INSERT INTO student(name,rollnumber) VALUES(?,?)",(studentNames,studentRollNos))
    conn.commit()


def selectFromDB():
    output =c.execute("SELECT * FROM student")
    print("type of output",type(output))
    data = output.fetchall()
    print("type of data is ", type(data),"data is : ",data)
    


createTable()
dynamicEntry()
selectFromDB()