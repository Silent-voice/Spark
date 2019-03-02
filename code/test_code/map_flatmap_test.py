# -*- coding:utf-8 -*-

from pyspark import SparkContext

def map_f(x):
    return x.split(' ')


def flatMap_f_1(x):
    return x.split(' ')


def flatMap_f_2(x):
    l1 = x.split(' ')
    l2 = []
    for i in l1:
        l2.append(list(i))

    return l2






sc = SparkContext('spark://master:7077', 'test')
rdd1 = sc.parallelize(["Hello World","Spark Hadoop Storm","java python c"])

rdd2 = rdd1.map(map_f)


rdd3 = rdd1.flatMap(flatMap_f_1)

rdd4 = rdd1.flatMap(flatMap_f_2)

print 'rdd2 : ' + str(rdd2.collect())
print 'rdd3 : ' + str(rdd3.collect())
print 'rdd4 : ' + str(rdd4.collect())

'''
rdd2 : [['Hello', 'World'], ['Spark', 'Hadoop', 'Storm'], ['java', 'python', 'c']]
rdd3 : ['Hello', 'World', 'Spark', 'Hadoop', 'Storm', 'java', 'python', 'c']
rdd4 : [['H', 'e', 'l', 'l', 'o'], ['W', 'o', 'r', 'l', 'd'], ['S', 'p', 'a', 'r', 'k'], ['H', 'a', 'd', 'o', 'o', 'p'], ['S', 't', 'o', 'r', 'm'], ['j', 'a', 'v', 'a'], ['p', 'y', 't', 'h', 'o', 'n'], ['c']]
'''