import pyspark

sc = pyspark.SparkContext()
rdd = sc.textFile('gs://bucket-kpi2/inputFolder/spikey_sales_weekly.csv')
no_of_rows = rdd.count()
print(no_of_rows)