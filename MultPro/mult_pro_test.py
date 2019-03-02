# -*- coding:utf-8 -*-


from multiprocessing import Pool
from pyspark.sql import SparkSession


def fun(sql_name):
    my_spark = SparkSession \
        .builder \
        .appName("myApp") \
        .config("spark.mongodb.input.uri", "mongodb://10.2.2.77/test."+sql_name) \
        .config("spark.mongodb.output.uri", "mongodb://10.2.2.77/test.test") \
        .getOrCreate()

    for i in range(10):
        df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
        df.show()


if __name__ == '__main__':
    db_pool = Pool(processes=3)
    db_pool.apply_async(fun, ['m1'])
    db_pool.apply_async(fun, ['m2'])
    db_pool.apply_async(fun, ['m3'])

    db_pool.close()
    db_pool.join()


