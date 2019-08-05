import logging
import urllib
import pandas as  pd
import pandas_gbq as pdgb
import os
import shutil
import datetime

logger = logging.getLogger()

def findNameAndEmpNoOfManagerOfSales(df1,df2):
    df3 = pd.merge(left=df1,right=df2,how="left",left_on='DEPTNO', right_on='DEPTNO')
    # df3 = df1.merge(df2, how='left', left_on='DEPTNO', right_on='DEPTNO')
    df4 = df3[df3["JOB"]=="MANAGER"]
    df5 = df3[df3["DNAME"]=="RESEARCH"]
    df6 = pd.merge(left=df4,right=df5,how="inner")
    print("findNameAndEmpNoOfManagerOfSales : ")
    print(df6[:][["ENAME","JOB","DNAME","EMPNO"]])



def findNameAndEmpNoOfManagerOfSalesAndResearch(df1,df2):
    df3 = pd.merge(left=df1,right=df2,how="left",left_on='DEPTNO', right_on='DEPTNO')
    # df3 = df1.merge(df2, how='left', left_on='DEPTNO', right_on='DEPTNO')
    df4 = df3[df3["JOB"]=="MANAGER"]
    df5 = df3[df3["DNAME"]=="RESEARCH"]
    df6 = pd.merge(left=df4,right=df5,how="inner")
    print("findNameAndEmpNoOfManagerOfSales : ")
    print(df6[:][["ENAME","JOB","DNAME","EMPNO"]])


def readCompleteFileAsString(fileName1 = "../fileHandling/src_file/input_data_spikey_sales_weekly.csv" ,fileName2 = "../fileHandling/src_file/input_data_spikey_sales_weekly.csv" ):
    df1 = pd.read_csv(fileName1)#, dtype={'Contact_Name': str}, low_memory=False)
    # print(df1)
    df2 = pd.read_csv(fileName2,delimiter=',')
    findNameAndEmpNoOfManagerOfSales(df1, df2)

    # print(df2)
    print(len(df1), len(df2))
    print(df1 + df2)
    print(len(df1+df2))
    df3 = pd.concat([df1,df2], axis=0)
    print(df3)
    # print(df3)
    df3_1 = pd.concat([df1, df2], axis=1)
    print("df3_1")
    print(df3_1)
    print(type(df3))
    print(df1.head())
    print(df2.head())
    # print(df3)
    # print(df3.groupby())


    print("find manager of SALES department")
    print(df1[:]["DNAME"]=="SALES")

    df4 = df1.merge(df2, how='left', left_on='DEPTNO', right_on='DEPTNO')
    print(df4.head())
    print("column names")
    print(df4.head())
    # print("manager of SALES department")
    df5 = df4[df4["DNAME"]=="SALES"]
    df6 = df4[df4["JOB"]=="MANAGER"]
    print(df5.head())
    print(df6.head())
    df5_6 = pd.merge(left=df5,right=df6,how="inner")
    print(df5_6)
    print(df5_6[:][["LOC","EMPNO"]])

    df7 = df4["DNAME"] == 'SALES'
    df8 = df4['JOB'] == 'MANAGER'
    df9 = df7 & df8
    print(df9[df9])
    # df6 = df4[df4["JOB"]=="MANAGER"]
    # print(df6)
    # # df6 = df1[:]["JOB"]=="MANAGER"
    # print(df5 and df6)
    # # print(df6)
    # df7 = df5 and df6
    # df1["DNAME"="SALES"][]


readCompleteFileAsString(fileName1 = "../fileHandling/src_file/dept_table.csv", fileName2 = "../fileHandling/src_file/emp_table.csv")

# readCompleteFileAsString(fileName = "../fileHandling/src_file/emp_table.csv")


# t=(1,2,3)
# print(t,type(t))
# t=([1,2,4],2,3)
# t2 = t+t
# print(t,type(t))