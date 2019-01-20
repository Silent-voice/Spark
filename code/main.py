# -*- coding:utf-8 -*-
import time
import datetime
import static
from methods import *
from pyspark import SparkContext
from dns import dns_control


if __name__ == '__main__':
    static._init()
    scan_interval = static.get_value('scan_interval')
    dns_data_dir_local_path = static.get_value('dns_data_dir_local_path')
    ssl_data_dir_local_path = static.get_value('ssl_data_dir_local_path')
    ftp_data_dir_local_path = static.get_value('ftp_data_dir_local_path')

    dns_data_dir_hdfs_path = static.get_value('dns_data_dir_hdfs_path')
    ssl_data_dir_hdfs_path = static.get_value('ssl_data_dir_hdfs_path')
    ftp_data_dir_hdfs_path = static.get_value('ftp_data_dir_hdfs_path')

    dns_feature_dir_hdfs_path = static.get_value('dns_feature_dir_hdfs_path')
    ssl_feature_dir_hdfs_path = static.get_value('ssl_feature_dir_hdfs_path')
    ftp_feature_dir_hdfs_path = static.get_value('ftp_feature_dir_hdfs_path')

    sc = SparkContext('spark://master:7077', 'ml')
    sc.addPyFile('/home/hadoop/spark_code/code/static.py')
    # sc.addPyFile('/home/hadoop/spark_code/code/methods.py')
    # sc.addPyFile('/home/hadoop/spark_code/code/dns/dns_control.py')
    sc.addPyFile('/home/hadoop/spark_code/code/dns/dns_methods.py')
    batch_id = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

    # dns_control = __import__('dns_control')
    dns_control.control(sc, dns_data_dir_hdfs_path, dns_feature_dir_hdfs_path, batch_id)

    # while True:
    #     dns_file_list = scan(dns_data_dir_local_path)
    #     ssl_file_list = scan(ssl_data_dir_local_path)
    #     ftp_file_list = scan(ftp_data_dir_local_path)
    #
    #     if dns_file_list == [] and ssl_file_list == [] and ftp_file_list == []:
    #         time.sleep(scan_interval)
    #         continue
    #     else:
    #         sc = SparkContext('spark://master:7077', 'ml')
    #
    #     batch_id = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    #     if dns_file_list != []:
    #         #TODO
    #         #将文件上传至HDFS
    #         upload_to_hdfs(dns_file_list, dns_data_dir_hdfs_path)
    #
    #         #对数据进行分布式处理
    #         dns_control.control(sc, dns_data_dir_hdfs_path, dns_feature_dir_hdfs_path, batch_id)
    #
    #         #删除已处理数据
    #         delete_local_files(dns_file_list)
    #
    #     if ssl_file_list != []:
    #         #TODO
    #         upload_to_hdfs(ssl_file_list, ssl_data_dir_hdfs_path)
    #
    #         delete_local_files(ssl_file_list)
    #
    #     if ftp_file_list != []:
    #         #TODO
    #         upload_to_hdfs(ftp_file_list, ftp_data_dir_hdfs_path)
    #
    #         delete_local_files(ftp_file_list)



