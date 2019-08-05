# import csv
# import urllib
#
# url = 'https://storage.cloud.google.com/resources_for_gcp_dwh/input_data/jtf_rs_salesreps.csv'
#
#
# response = urllib.urlopen(url)
# cr = csv.reader(response)
# # print cr
# i=0
# for row in cr:
#     print row
#     i += 1
#     if i == 50:
#         break

from google.cloud import storage
client = storage.Client()
bucket = client.get_bucket('resources_for_gcp_dwh')
blob = storage.Blob('input_data/jtf_rs_salesreps.csv', bucket)
content = str(blob.download_as_string().split("\r\n")[0].split('"')[:]).split(',')
# content = stage
print("content" ,content)

for item in content:
    print("item : ", item)


import pandas as pd


import binascii
import os
import uuid

import six
# import file_io
#
# with file_io.FileIO('gs://resources_for_gcp_dwh/input_data/jtf_rs_salesreps.csv', 'r') as f:
#   df2 = pd.read_csv(f)

# import StringIO
# temp_str = "gs://resources_for_gcp_dwh/input_data/jtf_rs_salesreps.csv"
# df = pd.read_csv(StringIO(temp_str))
# print(df)


import dask.dataframe as dd #Import
# temp_str = "gs://resources_for_gcp_dwh/input_data/jtf_rs_salesreps.csv"
temp_str = "gs://new-data-bucket/poc/hr_all_organization_units/2019-04-15"
dataframe = dd.read_csv(temp_str) #Read CSV data
print("dataframe :", dataframe[0])