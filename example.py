# example.py
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test").getOrCreate()
print(spark.version)

# Added comment line
