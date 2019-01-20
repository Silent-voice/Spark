import time
import datetime
import sys
import codecs
charList = {}
confFilePath = sys.path[0] + '/dns/charList.txt'
confFile = codecs.open(filename=confFilePath, mode='r', encoding='utf-8', errors='ignore')
lines = confFile.readlines()
i = 1
for line in lines:
    temp = line.strip('\n').strip('\r').strip(' ')
    if temp != '':
        charList[temp] = i
        i += 1

print charList