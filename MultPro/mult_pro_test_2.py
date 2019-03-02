# -*- coding:utf-8 -*-


from multiprocessing import Pool
from pyspark.sql import SparkSession


def fun(my_spark, sql_name):

    for i in range(10):
        df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri","mongodb://10.2.2.77/test."+sql_name).load()
        df.show()


if __name__ == '__main__':
    my_spark = SparkSession \
        .builder \
        .appName("myApp") \
        .config("spark.mongodb.input.uri", "mongodb://10.2.2.77/test.people") \
        .config("spark.mongodb.output.uri", "mongodb://10.2.2.77/test.test") \
        .getOrCreate()

    db_pool = Pool(processes=3)
    db_pool.apply_async(fun, [my_spark, 'm1'])
    db_pool.apply_async(fun, [my_spark, 'm2'])
    db_pool.apply_async(fun, [my_spark, 'm3'])

    db_pool.close()
    db_pool.join()


