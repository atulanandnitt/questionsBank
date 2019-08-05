import json
import logging
import os
from google.cloud import storage as gcs
import webapp2


from google.appengine.api import app_identity


def get_column_names():
    pass

def read_file(self, filename):
  self.response.write('Reading the full file contents:\n')

  gcs_file = gcs.open(filename)
  contents = gcs_file.read()
  gcs_file.close()
  self.response.write(contents)



def format_output_json():
    # abs_folder_location = "D:/notes/GCP/KPI/convertToPython/gcp-dwh/src/main/resources/bigquery-schemas/"
    # relative_folder_location_modified_json = "modified_schema/"
    abs_folder_location = "gs://resources_for_gcp_dwh/bigquery-schemas/"
    relative_folder_location_modified_json = "modified_schema/"
    relative_file_name = "jtf_rs_salesreps.json"
    abs_file_name = abs_folder_location + relative_folder_location_modified_json + relative_file_name
    row_indices = list()
    try:
        with open(abs_file_name, 'r') as json_file:
            data = json.load(json_file)

    except ValueError as err:
        print err.args

    for item in data:
        print(item["name"])


# format_output_json()