# -*- coding: utf-8 -*-
import os

def scan(dir_path):
    file_list = []
    fileName_list = os.listdir(dir_path)
    for fileName in fileName_list:
        file_path = dir_path + '/' + fileName
        if os.path.isfile(file_path):
            file_list.append(file_path)


    return file_list


def upload_to_hdfs(file_path_list, hdfs_dir_path):
    for file_path in file_path_list:
        cmd = '/usr/local/audr/bin/hdfs dfs -put ' + file_path + ' ' + hdfs_dir_path
        os.system(cmd)
    return

def delete_local_files(file_path_list):
    for file_path in file_path_list:
        os.remove(file_path)
    return



