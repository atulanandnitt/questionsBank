from google.cloud import bigquery
import pandas as pd
import os
import json



def getDetailsFromBQTable():
    client = bigquery.Client()

    def getResult3(sql_query):
        query_job = client.query(sql_query)

        results = query_job.result()  # Waits for job to complete.

        df3 = results.to_dataframe()
        return df3


    print("*********************************************validate data ")
    try:

        sql_query1 = """
                        SELECT * FROM `sr-dev-datahub.Datahub.FF_STG_WORK_DAY_HR_T_STG`  
                        where Status <>'Terminated'
                        and CANDIDATE_ID in 
                        (select  Associate_ID from  `sr-dev-datahub.Datahub.ADP_STG_HR_T`) 
                        order by CANDIDATE_ID
                    """

        df1_1 = getResult3(sql_query1)
        print(df1_1.head(1))
        # df1_1.to_csv("1_1.csv")
        print(df1_1.head(1))
        df1 = df1_1[["FIRST_NAME", "MIDDLE_NAME", "LAST_NAME"]]
        print(df1.head(2))
        # df1.to_csv("1.csv")

        print(df1.head(2))

    except:
        print "the query has issue, pls fix that 1st"




if __name__ == '__main__':
    print("getting data from both tables")
    getDetailsFromBQTable()
