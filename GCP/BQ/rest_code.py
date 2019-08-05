from google.cloud import bigquery
import EV
import os
import json


def getDetailsFromBQTable():
    client = bigquery.Client()
    project = EV.project_id
    dataset = EV.dataset_id
    apiName = "ENGAGE_USERS"
    table_T = "INVIEW_STG_CC_ENGAGE_EVALUATION_ANSWERS_T"
    table_TMP = "INVIEW_CC_ENGAGE_EVALUATION_ANSWERS_TMP"

    # apiName = "ENGAGE_EVALUATIONANSWERS"
    #apiName = "ENGAGE_EVALUATIONS"
    # table_T = "INVIEW_STG_CC_{0}_T".format(apiName)
    # table_TMP = "INVIEW_CC_{0}_TMP".format(apiName)
    #table_T = "INVIEW_STG_CC_ENGAGE_EVALUATIONSECTIONS_T"
    #table_TMP = 'INVIEW_CC_ENGAGE_EVALUATIONSECTIONS_TMP'
    # table_T = "INVIEW_STG_CC_ENGAGE_EVALUATIONS_T"
    # table_TMP = "INVIEW_CC_ENGAGE_EVALUATIONS_TMP"
    # table = "INVIEW_CC_ENGAGE_EVALUATIONS_TMP"
    # table = "INVIEW_STG_CC_ENGAGE_EVALUATIONS_T"
    #table ="INCONTACT_STG_CC_AGENT_STATE_LOG_T"
    def getCount(table):
        query_job = client.query("""
            SELECT
              count(*) as countTillNow
            FROM `{}.{}.{}`
            """.format(project, dataset, table))

        results = query_job.result()  # Waits for job to complete.

        for row in results:
            print("{0} ".format(row.countTillNow))



    def getFewRows(table):
        query_job = client.query("""
            SELECT
              *
            FROM `{}.{}.{}` LIMIT 2
            """.format(project, dataset, table))

        results = query_job.result()  # Waits for job to complete.

        for row in results:
            print("{0}".format(row))

        print("result is :")
        print(results)

    # def getSchemaDetails():
    #     cmd1 = """
    #                 bq query --nouse_legacy_sql
    #                 SELECT * EXCEPT(is_typed) FROM {}.{}.{}""".format(project, dataset, table)
    #
    #     try:
    #         load_result = os.popen(cmd1)
    #         print("load_result :", str(load_result))
    #     except IOError as ex:
    #         raise IOError("Error in reading config file: %s" % str("error found"))
    #     except ValueError as err:
    #         print
    #         err.args

    def getSchemaDetails2(table):
        """
        can be used to create json by exporint result into sepertate log file and save the content into a json file
        :return:
        """

        cmd1 = """bq show --schema --format=prettyjson {}:{}.{}""".format(project, dataset, table)

        try:
            results = os.popen(cmd1)
            print("load_result :", type(results))
            # results_json = json.dumps(results)
            # json_fileName = "atul_"+table+".json"
            # with open(json_fileName, 'w') as f1:
            #     json.dump(results_json, f1)

            for row in results:
                print("{0}".format(row))


        except IOError as ex:
            raise IOError("Error in reading config file: %s" % str("error found"))
        except ValueError as err:
            print
            err.args






    print("*********************************************validate : table_T")
    try:
     getCount(table_T)
     getFewRows(table_T)
     getSchemaDetails2(table_T)
    except:
     print("_T is not created yet")

    print("*********************************************validate : table_TMP")
    getCount(table_TMP)
    getFewRows(table_TMP)
    getSchemaDetails2(table_TMP)


if __name__=='__main__':
    getDetailsFromBQTable()
