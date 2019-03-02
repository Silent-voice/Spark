# -*- coding: utf-8 -*-
import sys
import codecs

def _init():
    global _global_dict
    _global_dict = {
                    'dns_db' : 'mongodb://ip/db_name.table_name',
                    'ssl_db': 'mongodb://ip/db_name.table_name',
                    'ftp_db': 'mongodb://ip/db_name.table_name',
                    'res_db': 'mongodb://ip/db_name.table_name',


                    # 本地路径
                    'dns_data_dir_local_path' : '/home/audr/code/ML_test/data/dns',
                    'ssl_data_dir_local_path': '/home/audr/code/ML_test/data/ftp',
                    'ftp_data_dir_local_path': '/home/audr/code/ML_test/data/ftp',

                    # HDFS 路径
                    'dns_data_dir_hdfs_path' : '/data/dns',
                    'dns_feature_dir_hdfs_path': '/feature/dns',
                    'dns_tempFile_dir_hdfs_path': '/tempFile/dns',

                    'ssl_data_dir_hdfs_path': '/data/ssl',
                    'ssl_feature_dir_hdfs_path': '/feature/ssl',
                    'ssl_tempFile_dir_hdfs_path': '/tempFile/ssl',

                    'ftp_data_dir_hdfs_path': '/data/ftp',
                    'ftp_feature_dir_hdfs_path': '/feature/ftp',
                    'ftp_tempFile_dir_hdfs_path': '/tempFile/ftp',


                    #扫描时间间隔
                    'scan_interval' : '10',


                    # DGA
                    'charList' : {'$': 84, '(': 89, ',': 63, '0': 53, '4': 57, '8': 61, '<': 64, '@': 82, 'D': 30, 'H': 34, 'L': 38, 'P': 42, 'T': 46, 'X': 50, '\\': 77, '`': 79, 'd': 4, 'h': 8, 'l': 12, 'p': 16, 't': 20, 'x': 24, '|': 78, '#': 83, "'": 71, '+': 94, '/': 67, '3': 56, '7': 60, ';': 69, '?': 68, 'C': 29, 'G': 33, 'K': 37, 'O': 41, 'S': 45, 'W': 49, '[': 73, '_': 92, 'c': 3, 'g': 7, 'k': 11, 'o': 15, 's': 19, 'w': 23, '{': 74, '"': 72, '&': 87, '*': 88, '.': 65, '2': 55, '6': 59, ':': 70, '>': 66, 'B': 28, 'F': 32, 'J': 36, 'N': 40, 'R': 44, 'V': 48, 'Z': 52, '^': 86, 'b': 2, 'f': 6, 'j': 10, 'n': 14, 'r': 18, 'v': 22, 'z': 26, '~': 80, '!': 81, '%': 85, ')': 90, '-': 91, '1': 54, '5': 58, '9': 62, '=': 93, 'A': 27, 'E': 31, 'I': 35, 'M': 39, 'Q': 43, 'U': 47, 'Y': 51, ']': 75, 'a': 1, 'e': 5, 'i': 9, 'm': 13, 'q': 17, 'u': 21, 'y': 25, '}': 76},

                    }


def set_value(key,value):
    _global_dict[key] = value


def get_value(key,defValue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defValue