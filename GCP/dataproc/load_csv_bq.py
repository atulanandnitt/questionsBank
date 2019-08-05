from __future__ import absolute_import
import json
import pprint
import subprocess
import pyspark
from pyspark.sql import SQLContext

sc = pyspark.SparkContext()

bucket = sc._jsc.hadoopConfiguration().get('fs.gs.system.bucket')
project = sc._jsc.hadoopConfiguration().get('fs.gs.project.id')
input_directory = 'gs://{}/hadoop/tmp/bigquery/pyspark_input'.format(bucket)


#read CSV:
rdd = sc.textFile('gs://bucket-kpi2/inputFolder/spikey_sales_weekly.csv')
no_of_rows = rdd.count()
print("no_of_rows :: ", no_of_rows)


# Output Parameters.
output_dataset = 'sales_dataset'
output_table = 'sales_output'

# Load data in from csv.
rdd_data = sc.textFile('gs://bucket-kpi2/inputFolder/spikey_sales_weekly.csv')

# Display 10 results.
pprint.pprint(rdd_data.take(15))

# Stage data formatted as newline-delimited JSON in Cloud Storage.
output_directory = 'gs://{}/hadoop/tmp/bigquery/pyspark_output'.format(bucket)
output_files = output_directory + '/part-*'

sql_context = SQLContext(sc)
(rdd_data.toDF(['col1','col2']).write.format('json').save(output_directory))

# Shell out to bq CLI to perform BigQuery import.
subprocess.check_call(
    'bq load --source_format NEWLINE_DELIMITED_JSON '
    '--replace '
    '--autodetect '
    '{dataset}.{table} {files}'.format(
        dataset=output_dataset, table=output_table, files=output_files
    ).split())

# Manually clean up the staging_directories, otherwise BigQuery
# files will remain indefinitely.
input_path = sc._jvm.org.apache.hadoop.fs.Path(input_directory)
input_path.getFileSystem(sc._jsc.hadoopConfiguration()).delete(input_path, True)
output_path = sc._jvm.org.apache.hadoop.fs.Path(output_directory)
output_path.getFileSystem(sc._jsc.hadoopConfiguration()).delete(
    output_path, True)