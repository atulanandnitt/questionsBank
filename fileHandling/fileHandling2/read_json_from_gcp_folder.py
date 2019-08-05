import logging
import os
import cloudstorage as gcs
import webapp2

from google.appengine.api import app_identity


def read_text_file(filename = 'gs://resources_for_gcp_dwh/input_data/input.txt',
        project_id = 'bigquery-poc-188207',
        service_account="D://notes/GCP/KPI/convertToPython/serviceAccount/bigquery-poc-188207-651384e6a91c.json"):

    try:
        gcs_file = gcs.open(filename)
        contents = gcs_file.read()
        gcs_file.close()

    except ValueError as err:
        print err.args

    print contents
    return contents

print read_text_file()


# def read_text_file(text_file = 'gs://resources_for_gcp_dwh/input_data/input.txt',
#         project_id = 'bigquery-poc-188207',
#         service_account="D://notes/GCP/KPI/convertToPython/serviceAccount/bigquery-poc-188207-651384e6a91c.json"):
#
#     try:
#         with open(text_file, 'rb') as f1:
#             data = f1.read()
#
#     except ValueError as err:
#         print err.args
#
#     print data
#     return data
#
# print read_text_file()

#
#
# def find_keys_from_gcp_folder(
#         json_file = 'gs://resources_for_gcp_dwh/input_data/spikey_sales_weekly.json',
#         project_id = 'bigquery-poc-188207'
#         ):
#
#     client = bigquery.Client(project_id)
#
#
#     data = dict()
#     try:
#         with open(json_file, 'r') as json_file:
#             data = json.load(json_file)
#
#     except ValueError as err:
#         print err.args
#
#     key_names = list()
#     for item in data:
#         key_names.append(item["name"])
#     # print data["name"]
#     return key_names
#
#
#
#
#
#
# def find_keys_from_local(
#         json_file = 'C:/Users/Atul Anand/PycharmProjects/BQ_POC_ETL_PY2/resources/atul_test/spikey_sales_weekly.json'):
#     data = dict()
#     try:
#         with open(json_file, 'r') as json_file:
#             data = json.load(json_file)
#
#     except ValueError as err:
#         print err.args
#
#     key_names = list()
#     for item in data:
#         key_names.append(item["name"])
#     # print data["name"]
#     return key_names
#
#
# # print("find keys form GCP : ")
# # print find_keys_from_gcp_folder()
# # print find_keys_from_local()
