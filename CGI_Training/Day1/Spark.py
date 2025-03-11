# Databricks notebook source
Spark Datasets
1. RDD (1D)
2. DataFrame 

# COMMAND ----------

data=([1,'Naval'],(2,'A'))
schema="id int,name string"

df=spark.createDataFrame(data,schema)

# COMMAND ----------

Spark is Lazy Evaluated 

# COMMAND ----------


