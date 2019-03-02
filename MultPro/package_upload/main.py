# -*- coding:utf-8 -*-
import time
import datetime
from pyspark import SparkContext
import sys

if __name__ == '__main__':
    print sys.path
    sc = SparkContext('spark://master:7077', 'ml')
    sc.addPyFile('./P.zip')

    print sys.path

    from dns import x
    rdd1 = sc.textFile('/data/dns')
    rdd2 = rdd1.map(x.method)

    rdd2.saveAsTextFile('/result/pk_up_test')


    sc.stop()
