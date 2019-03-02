from pyspark import SparkContext
import os

def f1(x):
    l = x.split(" ")
    i = 0
    while(os.path.exists('/home/audr/word_'+str(i)+'.txt')):
        i += 1
    f = open('/home/audr/word_'+str(i)+'.txt', 'w+')
    f.write(str(l))
    return l

sc = SparkContext('spark://master:7077', 'word_count')
file_path = 'hdfs:///test/word.txt'
textFile = sc.textFile(file_path)
wordCount = textFile.flatMap(f1).map(lambda word: (word,1)).reduceByKey(lambda a, b : a + b)
res = wordCount.collect()
print res