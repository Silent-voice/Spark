# -*- coding:utf-8 -*-
import codecs
import sys

import numpy as np
import Binary_with_attention

if __name__ == '__main__':
    mode = sys.argv[1]		#模式 0->LSTM+aTTENTION二分类训练  1->LSTM+aTTENTION二分类判别
    batch_size = int(sys.argv[2])
    epochs = int(sys.argv[3])
    srcFilePath = sys.argv[4]	#原始数据文件路径
    modelPath = sys.argv[5]		#模型文件保存路径或读取路

    resultFilePath = ''
    testDomainFilePath = ''
    testLabelFilePath = ''
    nb_classes = 2

    if mode == '1':
        resultFilePath = sys.argv[6]	# 判别结构保存路径
    else:
        # 用于训练时测试已训练好的模型的效果
        testDomainFilePath = sys.argv[6]	# 测试文件路径
        testLabelFilePath = sys.argv[7]		# 测试文件标签路径

    #读取配置文件
    charList = {}
    confFilePath = sys.path[0] + '/configFiles/charList.txt'
    confFile = codecs.open(filename=confFilePath, mode='r', encoding='utf-8', errors='ignore')
    lines = confFile.readlines()
    #字符序列要从1开始 0是填充字
    i = 1
    for line in lines:
        temp = line.strip('\n').strip('\r').strip(' ')
        if temp != '':
            charList[temp] = i
            i += 1


    max_features = i

    #设置批处理个数
    # batch_size = 100
    # epochs = 1

    #转换数据格式
    x_data_sum = []
    y_data_sum = []
    x_test_sum = []
    y_test_sum = []

    if mode == '0':
        srcFile = codecs.open(filename=srcFilePath, mode='r', encoding='utf-8', errors='ignore')
        lines = srcFile.readlines()
        for line in lines:
            if line.strip('\n').strip('\r').strip(' ') == '':
                continue

            x_data = []
            s = line.strip('\n').strip('\r').strip(' ').split(' ')
            x = str(s[0])
            y = int(s[1])

            for char in x:
                try:
                    x_data.append(charList[char])
                except:
                    print ('unexpected char' + ' : ' + char)
                    x_data.append(0)

            x_data_sum.append(x_data)
            y_data_sum.append(y)

        x_data_sum = np.array(x_data_sum)
        y_data_sum = np.array(y_data_sum)

        testDomainFile = codecs.open(filename=testDomainFilePath, mode='r', encoding='utf-8', errors='ignore')
        lines = testDomainFile.readlines()
        for line in lines:
            if line.strip('\n').strip('\r').strip(' ') == '':
                continue

            x_data = []
            x = str(line.strip('\n').strip('\r').strip(' '))
            for char in x:
                try:
                    x_data.append(charList[char])
                except:
                    print ('unexpected char' + ' : ' + char)
                    x_data.append(0)

            x_test_sum.append(x_data)

        testLableFile = codecs.open(filename=testLabelFilePath, mode='r', encoding='utf-8', errors='ignore')
        lines = testLableFile.readlines()
        for line in lines:
            if line.strip('\n').strip('\r').strip(' ') == '':
                continue

            y = line.strip('\n').strip('\r').strip(' ')
            y_test_sum.append(int(y))

        x_test_sum = np.array(x_test_sum)
        y_test_sum = np.array(y_test_sum)
        Binary_with_attention.train(max_features, x_data_sum, y_data_sum, x_test_sum, y_test_sum, batch_size, epochs, modelPath)
    elif mode == '1':
        srcFile = codecs.open(filename=srcFilePath, mode='r', encoding='utf-8', errors='ignore')
        lines = srcFile.readlines()
        for line in lines:
            if line.strip('\n').strip('\r').strip(' ') == '':
                continue

            x_data = []
            x = line.strip('\n').strip('\r').strip(' ')

            for char in x:
                try:
                    x_data.append(charList[char])
                except:
                    print ('unexpected char' + ' : ' + char)
                    x_data.append(0)

            x_data_sum.append(x_data)

        x_data_sum = np.array(x_data_sum)

        Binary_with_attention.predict(x_data_sum, batch_size, modelPath, resultFilePath)

    else:
        pass