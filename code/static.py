# -*- coding: utf-8 -*-
import sys
import codecs

def _init():
    global _global_dict
    _global_dict = {
                    # 本地路径
                    'dns_data_dir_local_path' : '',
                    'ssl_data_dir_local_path': '',
                    'ftp_data_dir_local_path': '',

                    # HDFS 路径
                    'dns_data_dir_hdfs_path' : '',
                    'dns_feature_dir_hdfs_path': '',
                    'dns_tempFile_dir_hdfs_path': '',

                    'ssl_data_dir_hdfs_path': '',
                    'ssl_feature_dir_hdfs_path': '',
                    'ssl_tempFile_dir_hdfs_path': '',

                    'ftp_data_dir_hdfs_path': '',
                    'ftp_feature_dir_hdfs_path': '',
                    'ftp_tempFile_dir_hdfs_path': '',


                    #扫描时间间隔
                    'scan_interval' : '',


                    # DGA
                    'charList' : {},

                    }

    charList = {}
    confFilePath = sys.path[0] + '/dns/charList.txt'
    confFile = codecs.open(filename=confFilePath, mode='r', encoding='utf-8', errors='ignore')
    lines = confFile.readlines()
    # 字符序列要从1开始 0是填充字
    i = 1
    for line in lines:
        temp = line.strip('\n').strip('\r').strip(' ')
        if temp != '':
            charList[temp] = i
            i += 1
    _global_dict['charList'] = charList




def set_value(key,value):
    _global_dict[key] = value


def get_value(key,defValue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defValue