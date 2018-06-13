#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wordcount import word_count_list
from wordcount import word_count_dict

if __name__ == '__main__':
    # 路径为绝对路径， 如/home/yuxuehai/Leslie/
    path = input("请输入正确的文件路径 \n")
    word_count_list(path)
    #word_count_dict(path)