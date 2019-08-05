from google.cloud import storage


def upload_blob(bucket_name="new-data-bucket-demo", source_blob_name="inputData.txt", destination_blob_name="inputData2.txt"):
    """Uploads a file to the bucket."""
    storage.Client().get_bucket(bucket_name).blob(destination_blob_name).upload_from_filename(source_blob_name)
    # storage_client = storage.Client()
    # bucket_obj = storage_client.get_bucket(bucket_name)
    # blob = bucket_obj.blob(destination_blob_name)
    # print(blob)
    # try:
    #     blob.upload_from_filename(source_file_name)
    # except IOError as ex:
    #     raise IOError("csv files couldnt get uploaded")
    # except ValueError as err:
    #     print err.args
    #
    # print 'File {} uploaded to {}.'.format(source_file_name, destination_blob_name)


def download_blob(bucket_name, source_blob_name, destination_blob_name):
    """Downloads a blob from the bucket."""
    storage.Client().get_bucket(bucket_name).blob(source_blob_name).download_to_filename(destination_blob_name)
    # storage_client = storage.Client()
    # bucket = storage_client.get_bucket(bucket_name)
    # blob = bucket.blob(source_blob_name)
    #
    # blob.download_to_filename(destination_file_name)
    #
    # print('Blob {} downloaded to {}.'.format(
    #     source_blob_name,
    #     destination_file_name))


source_file_name ="inputData.txt"
upload_blob(bucket_name="new-data-bucket-demo", source_blob_name=source_file_name, destination_blob_name="inputData2.txt")
# download_blob(bucket_name="new-data-bucket-demo", source_blob_name='inputData.txt', destination_blob_name='inputData_downloaded.txt')
