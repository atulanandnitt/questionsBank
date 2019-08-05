import argparse
import unicodedata
import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.transforms import combiners
from time import sleep
from collections import OrderedDict
import cx_Oracle as cx
import logging
import yaml
import cx_Oracle as cx
import os
from google.cloud import storage
from oauth2client import file
import logging


def copy_blob(bucket_name, blob_name, new_bucket_name):
    new_blob_name = blob_name
    """Copies a blob from one bucket to another with a new name."""
    storage_client = storage.Client()
    source_bucket = storage_client.get_bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.get_bucket(new_bucket_name)

    new_blob = source_bucket.copy_blob(
        source_blob, destination_bucket, new_blob_name)

    print('Blob {} in bucket {} copied to blob {} in bucket {}.'.format(
        source_blob.name, source_bucket.name, new_blob.name,
        destination_bucket.name))

copy_blob(bucket_name='new-data-bucket-demo', blob_name='poc/ar_adjustments_all/2019-04-15/2019-04-15 16:34:46.124000_ar_adjustments_all.csv', new_bucket_name='processed-data-bucket-demo')


def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()

    print('Blob {} deleted.'.format(blob_name))

# copy_blob(bucket_name='new-data-bucket', blob_name='poc/ar_adjustments_all/2019-04-15/2019-04-15 16:34:46.124000_ar_adjustments_all.csv', new_bucket_name='new-data-bucket-demo')


def move_blob(bucket_name, blob_name, new_bucket_name):
    copy_blob(bucket_name, blob_name, new_bucket_name)
    delete_blob(bucket_name, blob_name)

# move_blob(bucket_name='new-data-bucket-demo', blob_name='poc/ar_adjustments_all/2019-04-15/2019-04-15 16:34:46.124000_ar_adjustments_all.csv', new_bucket_name='processed-data-bucket-demo')