import argparse
import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from collections import OrderedDict
import logging

from apache_beam.io import WriteToText
import unicodedata
from apache_beam.transforms import combiners
from time import sleep
# python zagFile_1.py --runner DataflowRunner --project bigquery-poc-188207  --save_main_session True --temp_location gs://resources-poc-atul/temp --requirements_file req.txt --num_workers 4



product_revenue_schema = ''
columns_name = []
project_id = 'sr-dev-datahub'
table_name = "1811_ID4042_FILE06_dataflow"
dataset_name = 'test_dataset'


def find_product_revenue_schema_and_column_name():
    global product_revenue_schema
    global columns_name
    datatype = 'STRING'
    column_name_list = ['FIRST_NAME', 'MIDDLE_INITIAL', 'LAST_NAME', 'FILLER', 'GENERATIONAL_SUFFIX', 'ADDRESS', 'CITY', 'STATE', 'ZIP_CODE', 'ZIP_PLUS_4', 'FILLER_1_SPACE', 'CARRIER_ROUTE', 'NUMERIC_STATE_CODE', 'NUMERIC_COUNTY_CODE', 'DESIGNATED_MARKET_AREA_DMA', 'CORE_BASD_STATISTICL_AREACBSA', 'NIELSEN_COUNTY_SIZE', 'LATITUDE', 'LONGITUDE', 'CENSUS_BASIC_TRACT_NUMBER', 'CENSUS_BASC_TRACT_SUB_CODE_NUM', 'CENSUS_BASIC_BLOCK_GROUP', 'CENSUS_BLOCK_CODE', 'CENSUS_2010_EDUCATION_LEVEL', 'CENSUS_2010MEDIAN_AGEOFHSCHLDR', 'CENSUS_2010_PERCENT_WHITE', 'CENSUS_2010_PERCENT_HISPANIC', 'CENSUS_2010_PERCENT_BLACK', 'CENSUS_2010MEDIAN_HSCHLD_INCME', 'CENSUS_2010_INCOME_PERCENTILE', 'CENSUS_2010_PERCENT_HOMEOWNER', 'CENSUS_2010_MEDIAN_HOME_VALUE', 'CENSUS2010PRCNTSINGLFMLYDWELIG', 'CENSUS_2010_PERCENT_MOBILE_HMS', 'CNSUS2010PRCNTBLUECOLAR_EMPLYD', 'CNSUS2010PRCNTWHITECOLAREMPLYD', 'CENSUS_2010_PERCENT_MARRIED', 'CNSUS2010PRCNT_HSCHLDWTHCHLDRN', 'CNSUS2010AVG_NUMOF_AUTOMOBILES', 'CNSUS2010MEDINHHEFFECBUNGINCME', 'CNSUS2010PRCNTDIVRCEDORSEPRATD', 'CNSUS2010PRCNTMOTRVHICLOWNRSHP', 'CNSUS2010PRCNTABVE_POVRTYLEVEL', 'CNSUS2010PRCNTBELW_POVRTYLEVEL', 'CNSUS2010PRCNTMOVED_SINCE_2000', 'CNSUS2010PRCNTBUILT_2000ORLATR', 'CNSUS2010_SOCIOECONOMIC_SCORE', 'CNSUS2010POP_DENSTYSTTECENTILE', 'CNSUS2010POP_DENSTY_US_CENTILE', 'CENSUS_CODING_LEVEL', 'ONE_PER_ADDRESS', 'VERIFIED_NEW', 'VERIFIED_OLD', 'MAILABLE_RECORD', 'HOUSEHOLD_IDENTIFICATION_NUM', 'INDIVIDUAL_ID_NUMBER', 'FILLER_3_SPACES', 'GENDER', 'ORIGINAL_RACE_CODE', 'RACE_CODE', 'FAMILY_POSITION', 'PRESENCE_OF_ELDERLY_PARENT', 'LENGTH_OF_RESIDENCE', 'HOMEOWNER_STATUS', 'FILLER_4_SPACES', 'DWELLING_TYPE', 'ESTIMATED_HOUSEHOLD_INCOME_3', 'NET_WORTH_3', 'ZIP_LEVEL_HSCHLD_INCOME_DECILE', 'DUAL_INCOME_INDEX_3', 'MAIL_ORDER_RESPONDER', 'MAIL_ORDER_BUYER', 'FILLER_1_SPACE_1', 'NUMBER_OF_ADULTS_IN_HOUSEHOLD', 'NUMBER_OF_PERSONS_IN_HOUSEHOLD', 'NUMBER_OF_REPORTING_SOURCES', 'NUMBER_OF_CHILDREN', 'CHLDRN_PRESNT00_02YEARS_OF_AGE', 'CHLDRN_PRESNT03_05YEARS_OF_AGE', 'CHLDRN_PRESNT06_10YEARS_OF_AGE', 'CHLDRN_PRESNT11_15YEARS_OF_AGE', 'CHLDRN_PRESNT16_18YEARS_OF_AGE', 'PRESENCE_OF_CHILDREN', 'INDIVIDUAL_OCCUPATION', 'INDIVIDUAL_SPOUSE_OCCUPATION', 'SOHO_INDICATOR_INDIVIDUAL', 'SOHO_INDICATOR_HOUSEHOLD', 'ONLINE_ACCESS', 'TELEPHONE_NUMBER', 'TELEPHONE_PUBLICATION_DATE', 'DPV_STATUS', 'PUBLIC_HOUSING_ADDRESS', 'DSF_RESULT_SEASONAL', 'DSF_RESULT_VACANT', 'SEASONAL_EDUCATION_ADDRESS', 'ZIP4_HOME_VALUE', 'AGE', 'DATE_OF_BIRTH_MONTH', 'DATE_OF_BIRTH_DAY', 'DATE_OF_BIRTH_YEAR', 'BANK_CARD_NEW_ISSUE_DATE', 'BANK_CARD', 'RETAIL_CARD', 'CREDIT_ACTIVE', 'CREDIT_ACTIVE_STANDARD_RETAIL', 'CREDT_ACTV_LOW_END_DEPT_STRS', 'CREDT_ACTV_MAIN_STREET_RETAIL', 'CREDIT_ACTIVE_HIGH_END_RETAIL', 'CREDT_ACTV_TRVL_PRSNL_SERVICS', 'CREDIT_ACTIVE_SPECIALTY', 'CREDIT_ACTIV_SPECIALTY_APPAREL', 'CREDT_ACTV_FNANCIL_SRVICS_BNKG', 'CREDT_ACTV_FNANCIL_SRVICS_INS', 'CREDT_ACTV_FNANCILSRVICSCREDIT', 'CREDT_ACTV_CATLG_SHWROM_RETAIL', 'CREDT_ACTV_COMPUTER_ELECTRONCS', 'CREDIT_ACTIVE_FURNITURE', 'CREDIT_ACTV_HOMEOFFICE_SUPPLIS', 'CREDIT_ACTIVE_HOME_IMPROVEMENT', 'CREDIT_ACTIVE_MEMBERSHIP_WH', 'CREDIT_ACTIVE_SPORTNG_GOODS', 'CREDT_ACTV_TVMAIL_ORDER_PURCHS', 'CREDIT_ACTIVE_GROCERIES', 'CREDIT_ACTIVE_OIL_COMPANIES', 'CREDIT_ACTIVE_MISCELLANEOUS', 'CREDIT_ACTIVITY_LAST_POSTED_DT', 'CREDIT_ACTIVE_TRADE_LINES', 'CHILD_1_DATE_OF_BIRTH', 'CHILD_1_GENDER', 'CHILD_2_DATE_OF_BIRTH', 'CHILD_2_GENDER', 'CHILD_3_DATE_OF_BIRTH', 'CHILD_3_GENDER', 'CHILD_4_DATE_OF_BIRTH', 'CHILD_4_GENDER', 'PRESENCE_OF_COMPUTER_OWNER', 'EMAIL_ACCESS', 'REGISTERED_VOTER_PARTY', 'REGISTERED_VOTER_INDICATOR', 'CONGRESSIONAL_DISTRICT', 'HUNTING_AND_FISHING', 'BOATING', 'PRESENCE_OF_DONOR', 'PRESENCE_OF_DONOR_ANIMAL', 'PRESENCE_OF_DONOR_ARTS', 'PRESENCE_OF_DONOR_CHILDREN', 'PRESENCE_OF_DONOR_CONSERVATIVE', 'PRESENCE_OF_DONOR_ENVIRONMENT', 'PRESENCE_OF_DONOR_HEALTH', 'PRESENCE_OF_DONOR_HUMANITARIAN', 'PRESENCE_OF_DONOR_LIBERAL', 'PRESENCE_OF_DONOR_RELIGIOUS', 'PRESENCE_OF_DONOR_VETERANS', 'PRESENCE_OF_VETERAN', 'PRESENCE_OF_COLLEGE_GRADUATE', 'US_AIRCRAFT', 'PILOTS', 'ALL_TERRAIN_VEHICLES', 'SNOWMOBILES', 'CONCEALED_WEAPONS', 'HOME_VALUE_ADDRESS_LEVEL', 'LOAN_TO_VALUE_RATIO', 'EST_DISCRETIONRY_INCOM_PERCENT', 'ESTIMATED_HOUSEHOLD_DEBT_LEVEL', 'EST_HSCHLD_INVSTBLE_ASSETS', 'HOUSEHOLD_COMPOSITION', 'FAMILY_MEMBER_65_PLUS', 'FAMILY_MEMBER_60TO64', 'FAMILY_MEMBER_50TO59', 'FAMILY_MEMBER_40TO49', 'FAMILY_MEMBER_30TO39', 'FAMILY_MEMBER_20TO29', 'FAMILY_MEMBER_18TO19', 'FAMILY_MEMBER_UNDER_18', 'SHORT_TERM_LOAN_APPLICANTS', 'BANKRUPTCY_DOCKET_DATE', 'BANKRUPTCY_HOUSEHOLD_INDICATOR', 'BANKRUPTCY_INDIVDUAL_INDICATOR', 'PRESENCE_OF_SURVEY_DATA', 'SURVEY_OWN_OR_RENT', 'SURVEY_HOUSEHOLD_LEVEL_MATCH', 'SURVEY_INDIVIDUAL_LEVEL_MATCH', 'SURVY_HSCHLD_LEVELMATCH_ONLINE', 'SURVYINDVDUAL_LEVL_MATCH_ONLNE', 'SURVEY_DATA', 'SURVEY_DATE', 'SURVEY_DATE_ONLINE', 'SURVEY_GROUP', 'BUYER_CATALOG_LAST_ORDER_DATE', 'BUYR_CATLG_LST_ONLINEORDER_DT', 'BUYR_CATLG_LST_OFFLINEORDER_DT', 'BUYER_CATALOG_TOTAL_ORDERS', 'BUYER_CATALOG_TOTAL_DOLLARS', 'BUYER_CATALOG_ONLINE_ORDERS', 'BUYER_CATALOG_ONLINE_DOLLARS', 'BUYER_CATALOG_OFFLINE_ORDERS', 'BUYER_CATALOG_OFFLINE_DOLLARS', 'BUYER_CATALOG_AVG_ORDERDOLLARS', 'BUYR_CATALG_AVG_ONLINE_DOLLARS', 'BUYR_CATALG_AVG_OFLINE_DOLLARS', 'BUYER_DATA', 'BUYER_RETAIL_LAST_ORDER_DATE', 'BUYER_RETAIL_ORDERS', 'BUYER_RETAIL_DOLLARS', 'BUYER_DATA_1', 'BUYER_CATALOG_SPNDING_PATTERNS', 'GENERATIONS', 'MAIL_ORDER_RESPONDER_INSURANCE', 'RELIGION', 'COUNTRY_OF_ORIGIN', 'ASSIMILATION', 'ETHNIC_GROUP', 'ETHNICITY', 'LANGUAGE', 'ASSESSED_TOTAL_VALUE', 'ASSESSED_LAND_VALUE', 'PROPERTY_SALE_DATE', 'PROPERTY_SALE_PRICE', 'MORTGAGE_AMOUNT_1ST', 'MORTGAGE_LOAN_TYPE_CODE', 'MORTGAGE_TERM', 'MORTGAGE_AMOUNT_2ND', 'LIVING_SQUARE_FEET', 'YEAR_BUILT', 'EFFECTIVE_YEAR_BUILT', 'POOL', 'ROOF_TYPE', 'LAND_SQUARE_FOOTAGE', 'REAL_ESTATE_INVESTOR', 'DIGITAL_DESTINATIONS_GROUPS', 'DIGITAL_DEVICES', 'DIGITAL_DESTINATIONS', 'DIGITAL_NEIGHBORHOODS_2', 'RISK_SCORE', 'FILLER3SR', 'FILLER5SR', 'FILLER1SR', 'FILLER1SR_1', 'RESPONSE_MODEL_SCORE_OLDER', 'RESPONSE_MODEL_DECILE_OLDER', 'RESPONSE_MODEL_SCORE_YOUNGER', 'RESPONSE_MODEL_DECILE_YOUNGER', 'FILLER_10_SPACES_RESERVED_1', 'FILLER_10_SPACES_RESERVED_2', 'FILLER_10_SPACES_RESERVED_3', 'FILLER_10_SPACES_RESERVED_4', 'FILLER_10_SPACES_RESERVED_5', 'FILLER_10_SPACES_RESERVED_6', 'FILLER_5_SPACES_RESERVED_1', 'FILLER_10_SPACES_RESERVED_7', 'FILLER_10_SPACES_RESERVED_8', 'FILLER_10_SPACES_RESERVED_9', 'FILLER_10_SPACES_RESERVED_10', 'FILLER_10_SPACES_RESERVED_11', 'FILLER_10_SPACES_RESERVED_12', 'FILLER_10_SPACES_RESERVED_13', 'FILLER_5_SPACES_RESERVED_2', 'KLNK', 'FILLER_8_SPACES_RESERVED_1', 'FILLER_10_SPACES_RESERVED_14', 'FILLER_10_SPACES_RESERVED_15', 'FILLER_5_SPACES_RESERVED_3', 'FILLER_10_SPACES_RESERVED_16', 'FILLER_10_SPACES_RESERVED_17', 'FILLER_5_SPACES_RESERVED_4', 'FILLER_10_SPACES_RESERVED_18', 'FILLER_10_SPACES_RESERVED_19', 'FILLER_10_SPACES_RESERVED_20', 'FILLER_5_SPACES_RESERVED_5', 'FILLER_10_SPACES_RESERVED_21', 'FILLER_10_SPACES_RESERVED_22', 'FILLER_10_SPACES_RESERVED_23', 'FILLER_10_SPACES_RESERVED_24', 'FILLER_10_SPACES_RESERVED_25', 'FILLER_8_SPACES_RESERVED_2', 'FILLER_10_SPACES_RESERVED_26']
    for item in column_name_list:
        product_revenue_schema += item + ":" + datatype + ","
        columns_name.append(item)

    product_revenue_schema = product_revenue_schema[0:-1]

    return product_revenue_schema, columns_name


class Split(beam.DoFn):

    def process(self, element):
        element = element.encode('ascii', 'ignore').decode('ascii')
        logging.info("********************************inside process  : ")
        from google.cloud import storage
        storage_client = storage.Client()
        # get bucket with name
        bucket = storage_client.get_bucket('sunrun_mops')
        # get bucket data as blob
        blob = bucket.get_blob('Data_Dict_1409_latest.csv')
        # gs://sunrun_mops/Data_Dict_1409_latest.csv
        # convert to string
        csv_data = blob.download_as_string()
        logging.info("********************************read csv_data  : ")
        # print("json_data :", csv_data, type(csv_data))
        column_name = csv_data.split("\r\n")
        dict1 = OrderedDict()

        logging.info("********************************finding column names  : ")

        for column in column_name[1:]:
            logging.info(column)
            if len(column) > 0:
                column_name, start, end, length, dataType = column.split(",")
                start = int(start)
                end_corrected = int(end) + 1
                column_data = str(element[start:end_corrected])
                if len(column_data) > 0:
                    print(dict1)
                    dict1[column_name] = str(column_data)
                    logging.info("********************************dict1  : ")
                    logging.info(dict1)
                else:
                    logging.info("data for column {0} is not there.".format(column_name))

        return [dict1]


def run2(argv=None):
    print("inside run2")
    # print("product_revenue_schema: ", product_revenue_schema)
    # print("columns_name :", columns_name)
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_csv_file',
                        dest='input_csv_file',
                        default='gs://sunrun_mops/Ravi_test_1409',
                        help='Input file to process.')

    parser.add_argument('--input_json_file',
                        default='gs://resources-poc-atul/data/1811_ID4042_FILE04.json',
                        # required=True,
                        help='Input file to process.')

    parser.add_argument('--output_bq',
                        dest='output_bq',
                        # required=True,
                        default='{0}:{1}.{2}'.format(project_id,dataset_name,table_name),
                        # ':.ar_adjustments_all',
                        help='Output file to write results to.')

    parser.add_argument('--job_name',
                        dest='job_name',
                        default='job4',
                        help='Output file to write results to.')

    known_args, pipeline_args = parser.parse_known_args(argv)

    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = True

    with beam.Pipeline(options=pipeline_options) as p1:
        data_csv = p1 | 'Read zag file' >> ReadFromText(known_args.input_csv_file)
        dict1 = (data_csv | 'create dict from zag file' >> (beam.ParDo(Split())))
        (dict1 | 'Write to mydataset' >> beam.io.WriteToBigQuery(known_args.output_bq, schema=product_revenue_schema))


if __name__ == '__main__':
    print("find product_revenue_schema ")
    product_revenue_schema, columns_name = find_product_revenue_schema_and_column_name()
    print("started loading zag file top10lines")
    run2()


#