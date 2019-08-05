def readJson_from_GCS():
    from google.cloud import storage
    # create storage client
    storage_client = storage.Client()#.from_service_account_json('/Users/ey/testpk.json')
    # get bucket with name
    bucket = storage_client.get_bucket('resources-poc-atul')
    # get bucket data as blob
    blob = bucket.get_blob('data/Data_Dict_1409_atul.csv')
    # convert to string
    csv_data = blob.download_as_string()

    print("json_data :", csv_data, type(csv_data))
    column_name = csv_data.split("\r\n")

    for column in column_name:
        print(column)
        break

readJson_from_GCS()


import pandas as pd
import xlrd, json, os

def create_df():
    n = 1251
    abs_file_name = "C:/Users/Atul Anand/PycharmProjects/BQ_POC_ETL_PY2/objective_clarifications/dataFlow/Data_Dict_1409_atul.xlsx"
    wb = xlrd.open_workbook(abs_file_name)
    sheet = wb.sheet_by_index(0)

    with open('{0}'.format(abs_file_name), 'r') as fr:
        assert n > 0
        while True:
            data = fr.read(n)
            if data == '':
                break
            list1 = list()
            for i in range(1, sheet.nrows):
                start = int(sheet.cell_value(i, 1))
                end = int(sheet.cell_value(i, 2) + 1)

                list1.append(data[start:end].strip())
            t1 = tuple(list1)
            rows_to_insert = [
                t1
            ]

            print("list1 : ", list1)
            break

# create_df()
