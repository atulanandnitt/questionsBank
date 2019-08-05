from google.cloud import bigquery
import pandas as pd
import os
import json


def getDetailsFromBQTable():
    client = bigquery.Client()

    def getResult1():
        query_job = client.query("""
            SELECT * FROM `sr-dev-datahub.Datahub.FF_STG_WORK_DAY_HR_T_STG`
            where Status <>'Terminated'
            and CANDIDATE_ID in (select  Associate_ID from  `sr-dev-datahub.Datahub.ADP_STG_HR_T`) order by CANDIDATE_ID
            """)

        results = query_job.result()  # Waits for job to complete.

        df1 = results.to_dataframe()
        print(df1.head(2))
        print(type(df1))

        return df1

    def getResult2():
        query_job = client.query("""
            SELECT * FROM `sr-dev-datahub.Datahub.ADP_STG_HR_T`
            where Position_Status <>'Terminated'
            and Associate_ID in (select CANDIDATE_ID from  Datahub.FF_STG_WORK_DAY_HR_T_STG) order by Associate_ID
            """)
        results = query_job.result()  # Waits for job to complete.

        df2 = results.to_dataframe()
        print(df2.head(2))
        print(type(df2))

        return df2
        # df2 = client.query(query_job).to_dataframe()
        # df2.sort_values(by= 'Associate_ID')
        # return df2

    print("*********************************************validate data ")
    try:
        df1 = getResult1()
        df2 = getResult2()
        df3 = pd.DataFrame()
        # min = a if a < b else b
        print(df1.head())
        print("df2 is ")
        print(df2.head())
        larger = df1 if len(df1) > len(df2) else df2
        smaller = df1 if len(df1) < len(df2) else df2
        for i in range(len(smaller)):
            if df1.loc[i, "FIRST_NAME"] == df2.loc[i, "First_Name"]:
                df3.loc[i, "FIRST_NAME"] = True
            else:
                df3.loc[i, "FIRST_NAME"] = False

            col_name = "MIDDLE_NAME"

            if df1.loc[i, col_name] == df2.loc[i, col_name]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False

            col_name = "LAST_NAME"
            if df1.loc[i, col_name] == df2.loc[i, col_name]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False

            col_name = "STATUS"

            if df1.loc[i, col_name] == df2.loc[i, col_name]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False

            col_name = "JOB_FUNCTION_CODE"
            if df1.loc[i, col_name] == df2.loc[i, col_name ]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False

            col_name = "CANDIDATE_ID"

            if df1.loc[i, col_name] == df2.loc[i, "Associate_ID"]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False

            col_name = "DOB"

            if df1.loc[i, col_name] == df2.loc[i, "Birth_Date"]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False

            col_name = "SUPERVISOR_EMAIL_ADDRESS"
            if df1.loc[i, col_name] == df2.loc[i, "SR_Email"]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False

            col_name = "EMPLOYEE_FILE_NUM"
            if df1.loc[i, col_name] == df2.loc[i, "File_Number"]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False
            col_name = "Status"
            if df1.loc[i, col_name] == df2.loc[i, "Position_Status"]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False

            col_name = "BUSINESS_CARD_JOB_TITLE"
            if df1.loc[i, col_name] == df2.loc[i, "BusinessCardTitle"]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False



            col_name = "JOB_DESCRIPTION"
            if df1.loc[i, col_name] == df2.loc[i, col_name]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False


            col_name = "JOB_TITLE"
            if df1.loc[i, col_name] == df2.loc[i, "Job_Title_Code"]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False


            col_name = "EFFECTIVE_START_DT"
            if df1.loc[i, col_name] == df2.loc[i, "Position_Start_Date"]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False

            col_name = "EFFECTIVE_END_DT"
            if df1.loc[i, col_name] == df2.loc[i, "Position_Effective_End_Date"]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False

            col_name = "HOME_DEPARTMENT_CODE"
            if df1.loc[i, col_name] == df2.loc[i, "Home_Department_Code"]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False

            col_name = "PAY_GRADE_CODE"
            if df1.loc[i, col_name] == df2.loc[i, "Pay_Grade_Code"]:
                df3.loc[i, col_name] = True
            else:
                df3.loc[i, col_name] = False

        df4 = pd.concat([df1, df2, df3], axis=1)
        df4.to_csv("result.csv")


    except:
        print "either of the query has issue, pls fix that 1st"




if __name__ == '__main__':
    print("reading both tables")
    getDetailsFromBQTable()
