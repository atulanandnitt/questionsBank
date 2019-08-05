import beatbox
import pandas as pd
import dask.dataframe as dd

sf_username = "crackjeeonline@gmail.com"
sf_password = "sharedPassword1"
sf_api_token = "5m27qE6F8tIwLTyz4BooklCzg"

def find_all_lead_store_locally():
    sf_client = beatbox.PythonClient()
    password = str("%s%s" % (sf_password, sf_api_token))
    sf_client.login(sf_username, password)
    records = list()
    lead_qry = "SELECT id, Email, FirstName, LastName, OwnerId FROM Lead"
    records = sf_client.query(lead_qry)
    print("records :", type(records))
    df = pd.DataFrame(records)
    file_name = "data_from_sf.csv"
    df.to_csv(file_name, sep='|', encoding='utf-8')
    print(df)
    return records


def find_all_lead_store_GCS(csv_data_file_name="csv_data_from_sf"):
    sf_client = beatbox.PythonClient()
    password = str("%s%s" % (sf_password, sf_api_token))
    sf_client.login(sf_username, password)
    records = list()
    lead_qry = "SELECT id, Email, FirstName, LastName, OwnerId FROM Lead"
    records = sf_client.query(lead_qry)
    print("records :", type(records))
    df = pd.DataFrame(records)
    ddf = dd.from_pandas(df, npartitions=1)
    fileName = 'gs:\\\\resources_for_gcp_dwh\\new_data\\' + csv_data_file_name + '.csv'
    dd.to_csv(ddf, fileName, index=False, header=False, sep='|')

    return records


# find_all_lead_store_locally()
csv_data_file_name = "csv_data_from_sf"
# find_all_lead_store_locally()
find_all_lead_store_GCS(csv_data_file_name = csv_data_file_name)



# def get_lead_records_by_email(emailList):
#     sf_client = beatbox.PythonClient()
#     password = str("%s%s" % (sf_password, sf_api_token))
#     sf_client.login(sf_username, password)
#     records = list()
#     for email in emailList:
#         # lead_qry = "SELECT id, Email, FirstName, LastName, OwnerId FROM Lead WHERE Email = '%s'" % (email)
#         lead_qry = "SELECT id, Email, FirstName, LastName, OwnerId FROM Lead
#         data = sf_client.query(lead_qry)
#         if len(str(data)) > 0:
#             records.append(data)
#     return records
#
# # email = 'atullead.nitt@gmail.com'
# emailList = ["crackjeeonline@gmail.com",'atullead@gmail.com']
# print(get_lead_records_by_email(emailList))