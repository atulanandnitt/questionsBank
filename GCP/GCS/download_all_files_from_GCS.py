# # D:\notes\GCP\KPI\convertToPython\serviceAccount\***.json
# GOOGLE_APPLICATION_CREDENTIALS

from google.cloud import storage

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


# source_file_name ="inputData.txt"

    # download_blob(bucket_name="new-data-bucket-demo", source_blob_name='inputData.txt', destination_blob_name='inputData_downloaded.txt')


def find_list_all_csvs(bucket_name):
    # service_account = 'D://notes/GCP/KPI/convertToPython/serviceAccount/dataproc-sr-dev-datahub-a7a1e13add7e.json'
    storage_client = storage.Client()#.from_service_account_json(service_account)
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()

    for blob in blobs:
        download_blob(bucket_name, blob, blob)
        break


def main():
    # bucket_name="us-central1-bidev-cloud-com-2c706449-bucket"
    # bucket_name="sunrun_mops"
    bucket_name= "resources-poc-atul"
    find_list_all_csvs(bucket_name)


if __name__ == '__main__':
    print("starting download from bucket : sunrun_mops")
    main()
