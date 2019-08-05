import pandas as pd
import xlrd

#add 2 dataframe from XLS and csv


def readCompleteFileAsString(fileName = "../fileHandling/src_file/input_XLS.xls"):
    workbook = xlrd.open_workbook(fileName)
    worksheet = workbook.sheet_by_name('Sheet1')
    # worksheet = workbook.sheet_by_index(0)
    print("workbook", workbook)
    print("worksheet :", worksheet)
    print("read ", fileName)


# readCompleteFileAsString()


def readCompleteXLSFileAsString(fileName = "../fileHandling/src_file/input_XLS.xls"):
    data = pd.read_excel(fileName)
    print(data)
    print(type(data))


readCompleteXLSFileAsString()

