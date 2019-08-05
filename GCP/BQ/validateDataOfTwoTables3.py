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
                        and CANDIDATE_ID in (select  Associate_ID from  `sr-dev-datahub.Datahub.ADP_STG_HR_T`) order by CANDIDATE_ID
                    """

        sql_query2 = """
                        SELECT * FROM `sr-dev-datahub.Datahub.ADP_STG_HR_T`
                        where Position_Status <>'Terminated'
                        and Associate_ID in (select CANDIDATE_ID from  `sr-dev-datahub.Datahub.FF_STG_WORK_DAY_HR_T_STG`) order by Associate_ID
                    """

        df1_1 = getResult3(sql_query1)
        # df2_1 = getResult3(sql_query2)

        df1_1.to_csv("1_1.csv", sep='|')
        # df2_1.to_csv("2_1.csv", sep='|')
        # df1 = df1_1["FIRST_NAME","MIDDLE_NAME","LAST_NAME","JOB_FUNCTION_CODE","CANDIDATE_ID","DOB","SUPERVISOR_EMAIL_ADDRESS","EMPLOYEE_FILE_NUM", "Status", "BUSINESS_CARD_JOB_TITLE", "JOB_DESCRIPTION", "JOB_TITLE", "EFFECTIVE_START_DT", "EFFECTIVE_END_DT", "HOME_DEPARTMENT_CODE", "PAY_GRADE_CODE" ]
        # df2 = df2_1[
        #     "FIRST_NAME", "MIDDLE_NAME", "LAST_NAME", "JOB_FUNCTION_CODE", "Associate_ID", "Birth_Date", "SR_Email", "File_Number", "Position_Status", "BusinessCardTitle", "JOB_DESCRIPTION", "Job_Title_Code", "Position_Start_Date", "Position_Effective_End_Date", "HOME_DEPARTMENT_CODE", "PAY_GRADE_CODE"]
        df1 = df1_1["FIRST_NAME","MIDDLE_NAME","LAST_NAME","JOB_FUNCTION_CODE","CANDIDATE_ID","DOB"]
        # df2 = df2_1["First_Name", "Middle_Name", "Last_Name", "Job_Function_Code", "Associate_ID", "Birth_Date"]
        print(df1.head(2))
        df1.to_csv("1.csv", sep='|')
        # df2.to_csv("2.csv", sep='|')

        df3 = pd.DataFrame()

        print(df1.head(2))
        # print(df2.head(2))
        # larger = df1 if len(df1) > len(df2) else df2
        # smaller = df1 if len(df1) < len(df2) else df2
        # for i in range(len(smaller)):
        #     if df1.loc[i, "FIRST_NAME"] == df2.loc[i, "First_Name"]:
        #         df3.loc[i, "FIRST_NAME"] = True
        #     else:
        #         df3.loc[i, "FIRST_NAME"] = False
        #
        #     col_name = "MIDDLE_NAME"
        #
        #     if df1.loc[i, col_name] == df2.loc[i, col_name]:
        #         df3.loc[i, col_name] = True
        #     else:
        #         df3.loc[i, col_name] = False
        #
        #     col_name = "LAST_NAME"
        #     if df1.loc[i, col_name] == df2.loc[i, col_name]:
        #         df3.loc[i, col_name] = True
        #     else:
        #         df3.loc[i, col_name] = False

            #
            # col_name = "JOB_FUNCTION_CODE"
            # if df1.loc[i, col_name] == df2.loc[i, col_name ]:
            #     df3.loc[i, col_name] = True
            # else:
            #     df3.loc[i, col_name] = False
            #
            # col_name = "CANDIDATE_ID"
            #
            # if df1.loc[i, col_name] == df2.loc[i, "Associate_ID"]:
            #     df3.loc[i, col_name] = True
            # else:
            #     df3.loc[i, col_name] = False
            #
            # col_name = "DOB"
            #
            # if df1.loc[i, col_name] == df2.loc[i, "Birth_Date"]:
            #     df3.loc[i, col_name] = True
            # else:
            #     df3.loc[i, col_name] = False
            #
            # col_name = "SUPERVISOR_EMAIL_ADDRESS"
            # if df1.loc[i, col_name] == df2.loc[i, "SR_Email"]:
            #     df3.loc[i, col_name] = True
            # else:
            #     df3.loc[i, col_name] = False
            #
            # col_name = "EMPLOYEE_FILE_NUM"
            # if df1.loc[i, col_name] == df2.loc[i, "File_Number"]:
            #     df3.loc[i, col_name] = True
            # else:
            #     df3.loc[i, col_name] = False
            # col_name = "Status"
            # if df1.loc[i, col_name] == df2.loc[i, "Position_Status"]:
            #     df3.loc[i, col_name] = True
            # else:
            #     df3.loc[i, col_name] = False
            #
            # col_name = "BUSINESS_CARD_JOB_TITLE"
            # if df1.loc[i, col_name] == df2.loc[i, "BusinessCardTitle"]:
            #     df3.loc[i, col_name] = True
            # else:
            #     df3.loc[i, col_name] = False
            #
            #
            #
            # col_name = "JOB_DESCRIPTION"
            # if df1.loc[i, col_name] == df2.loc[i, col_name]:
            #     df3.loc[i, col_name] = True
            # else:
            #     df3.loc[i, col_name] = False
            #
            #
            # col_name = "JOB_TITLE"
            # if df1.loc[i, col_name] == df2.loc[i, "Job_Title_Code"]:
            #     df3.loc[i, col_name] = True
            # else:
            #     df3.loc[i, col_name] = False
            #
            #
            # col_name = "EFFECTIVE_START_DT"
            # if df1.loc[i, col_name] == df2.loc[i, "Position_Start_Date"]:
            #     df3.loc[i, col_name] = True
            # else:
            #     df3.loc[i, col_name] = False
            #
            # col_name = "EFFECTIVE_END_DT"
            # if df1.loc[i, col_name] == df2.loc[i, "Position_Effective_End_Date"]:
            #     df3.loc[i, col_name] = True
            # else:
            #     df3.loc[i, col_name] = False
            #
            # col_name = "HOME_DEPARTMENT_CODE"
            # if df1.loc[i, col_name] == df2.loc[i, "Home_Department_Code"]:
            #     df3.loc[i, col_name] = True
            # else:
            #     df3.loc[i, col_name] = False
            #
            # col_name = "PAY_GRADE_CODE"
            # if df1.loc[i, col_name] == df2.loc[i, "Pay_Grade_Code"]:
            #     df3.loc[i, col_name] = True
            # else:
            #     df3.loc[i, col_name] = False

        # df4 = pd.concat([df1, df2, df3], axis=1)
        # df4.to_csv("result.csv")


    except:
        print "either of the query has issue, pls fix that 1st"




if __name__ == '__main__':
    print("getting data from both tables")
    getDetailsFromBQTable()
