#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from collections import Counter

def word_count(path):
    sumsdata = []
    cnt = Counter()
    for fileName in os.listdir(path):
        print("filename: " + fileName)
        if os.path.isfile(fileName) and fileName.endswith(".txt"):
            print("filename: " + fileName)
            pathName = path + "/" +fileName
            with open(pathName, 'r') as br:
                data = br.readlines()
                print(data)
                br.close()
            sumsdata += [line.strip().lower() for line in data]
            print(sumsdata)

    for word in sumsdata:
        cnt[word] += 1
    cnt = dict(cnt)
    print(cnt)
    return cnt

def list_path(path):
    dirs = os.listdir(path)
    for file in dirs:
        print(file)

if __name__ == '__main__':
    #path = input("请输入正确的文件路径 \n")
    word_count("/home/yuxuehai/Leslie")
    # for key, value in cnt.items():
    #     print(key + ": " + str(value))
    #list_path(path)