# -*- coding:utf-8 -*-
from pyspark.sql import SparkSession




# mangodb

#创建session
my_spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", "mongodb://input_ip/test.input") \
    .config("spark.mongodb.output.uri", "mongodb://output_ip/test.output") \
    .getOrCreate()


# 从默认配置中指定的input db中读取数据
df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
# 重新指定数据库uri
df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri","mongodb://new_ip/people.contacts").load()


# 打印df
df.show()

# 写入数据库
# 四种模式 overwrite ignore errorifexists append
'''
overwrite : 先删除mongodb中指定的表，然后把数据写到这个表中
ignore : 如果mongodb中有这个表，就不写数据了，且不会报错
errorifexists : 如果mongodb中存在这个表就报错，如果不存在就正常写入
append : 不管mongodb中这个表存不存在直接往里写数据
'''
new_data = my_spark.createDataFrame([("Bilbo Baggins",  50), ("Gandalf", 1000), ("Thorin", 195)], ["name", "age"]) # 第一个参数是数据，第二个是字段名
new_data.write.format("com.mongodb.spark.sql.DefaultSource").mode("append").save()


# 按照限制读取数据
# 这里限制条件的写法和普通mangodb操作的写法相同
# age == 100
pipeline = "{'$match': {'age': 100}}"
df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").option("pipeline", pipeline).load()


# 70 < age <= 90
pipeline = "{'$match': {'age': { $gt : 70, $lte : 90 }}}"
df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").option("pipeline", pipeline).load()

#


