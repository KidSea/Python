#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from collections import Counter
import datetime

# 返回为字典形式
def word_count_dict(path):
    # 开始时间
    start = datetime.datetime.now()
    # 存储文件里的数据
    sumsdata = []
    # 计算个数
    cnt = Counter()
    # 从文件中获取数据
    for fileName in os.listdir(path):
        #print("filename: " + fileName)
        if os.path.isfile(fileName) and fileName.endswith(".txt"):
            #print("filename: " + fileName)
            pathName = path + "/" +fileName
            with open(pathName, 'r') as br:
                data = br.readlines()
                #print(data)
                br.close()
            sumsdata += [line.strip().lower() for line in data]
            #print(sumsdata)
    #将数据转换为字典
    for word in sumsdata:
        cnt[word] += 1
    cnt = dict(cnt)
    # 结束时间
    end = datetime.datetime.now()
    time = (end - start)
    # 打印时间
    print("run time is :" + str(time))
    # 打印字典
    print(cnt)
    return cnt

# 返回为列表形式
def word_count_list(path):
    start = datetime.datetime.now()
    sumsdata = []
    cnt = Counter()
    for fileName in os.listdir(path):
        #print("filename: " + fileName)
        if os.path.isfile(fileName) and fileName.endswith(".txt"):
            #print("filename: " + fileName)
            pathName = path + "/" +fileName
            with open(pathName, 'r') as br:
                data = br.readlines()
                #print(data)
                br.close()
            sumsdata += [line.strip().lower() for line in data]
            #print(sumsdata)

    for word in sumsdata:
        cnt[word] += 1
    cnt = dict(cnt)
    list = []
    # 将字典数据转换为列表
    for value in cnt:
        temp = [1,2]
        temp[0] = value
        temp[1] = cnt[value]
        list.append(temp)
    #list = [['1',1],['2',3]]
    end = datetime.datetime.now()
    time = (end - start)
    print("run time is :" + str(time))
    # 打印列表
    print(list)
    return list

def list_path(path):
    dirs = os.listdir(path)
    for file in dirs:
        print(file)

# if __name__ == '__main__':
#     # 路径为绝对路径， 如/home/yuxuehai/Leslie/
#     path = input("请输入正确的文件路径 \n")
#     word_count_list(path)