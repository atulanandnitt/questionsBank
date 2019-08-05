import cx_Oracle as cx
import pandas as pd
import time
import os, shutil

from datetime import datetime
from google.cloud import storage
import dask.dataframe as dd

class EBS_To_GCS():
    def __init__(self):
        self.con = cx.connect("GCP_BQ_POC/Admin123@52.229.14.226:1521/orcldb")
        self.cur = self.con.cursor()
        # self.filepath = 'D:/notes/GCP/KPI/convertToPython/gcp-dwh/src/main/resources/tableMetadata.csv'
        self.filepath = "D:/notes/GCP/KPI/convertToPython/gcp-dwh/src/main/resources/scripts/KPI_ANALYTICS/tableMetadata_allTables.csv"
        self.dirpath = "C:/Users/Atul Anand/PycharmProjects/BQ_POC_ETL/resources/data_csv/"
        # self.bucketname = "bigquery-poc-ankur"
        self.bucketname = "resources_for_gcp_dwh"
        self.new_data = "new_data"

    def clear_directory(self, folder=None):
        if folder == None:
            folder = self.dirpath
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print e

    def get_csv_gcs(self, type='fullLoad'):
        if type == 'fullLoad':
            count = 0
            with open(self.filepath, 'r') as fr:
                next(fr)
                self.clear_directory()
                for line in fr:
                    table_name, primary_key = line.split(',')
                    print("table_name : ", table_name)
                    query = "select * from " + table_name
                    self.cur.execute(query)
                    df = pd.DataFrame(list(self.cur))
                    ddf = dd.from_pandas(df, npartitions=1)
                    fileName = 'gs://resources_for_gcp_dwh/new_data/'+ table_name
                    dd.to_csv(ddf, fileName ,index=False, header=False)

    def get_csv_local(self, type='fullLoad'):
        if type == 'fullLoad':
            count = 0
            with open(self.filepath, 'r') as fr:
                next(fr)
                self.clear_directory()
                for line in fr:
                    table_name, primary_key = line.split(',')
                    print("table_name : ", table_name)
                    self.cur.execute("select * from " + table_name)
                    df = pd.DataFrame(list(self.cur))
                    df.to_csv(
                        r'C:/Users/Atul Anand/PycharmProjects/BQ_POC_ETL/resources/data_csv/' + table_name + '.csv',
                        index=None, header=False, sep='|', encoding='utf-8')


if __name__ == '__main__':
    obj = EBS_To_GCS()
    # obj.get_csv_gcs(type='fullLoad')
    obj.get_csv_local()
