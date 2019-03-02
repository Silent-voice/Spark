# -*- coding: utf-8 -*-
from pyspark import SparkContext

def control(sc, dns_data_dir_hdfs_path, dns_feature_dir_hdfs_path, batch_id):
    # sc = SparkContext.getOrCreate()
    # sc = SparkContext.getOrCreate('spark://master:7077', 'ml')

    dns_methods = __import__('dns_methods')

    dns_data_rdd = sc.textFile(dns_data_dir_hdfs_path)

    id_domain_rdd = dns_data_rdd.map(dns_methods.extract_id_domain)
    id_domain_rdd.cache()

    domain_vec_rdd = id_domain_rdd.map(dns_methods.domain_to_vec).reduceByKey(lambda x,y : x)
    domain_vec_rdd.cache()

    domain_res_rdd = domain_vec_rdd.mapPartitions(dns_methods.domain_predict)
    domain_res_rdd.saveAsTextFile(dns_feature_dir_hdfs_path + '/' + batch_id + '_domain_res')

    id_domain_rdd.saveAsTextFile(dns_feature_dir_hdfs_path + '/' + batch_id + '_id_domain')
    domain_vec_rdd.saveAsTextFile(dns_feature_dir_hdfs_path + '/' + batch_id + '_domain_vec')
    id_domain_rdd.unpersist()
    domain_vec_rdd.unpersist()


    return