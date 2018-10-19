#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num = [4, 11, 20, 18, 12, 5, 7, 8, 9, 10, 13, 3, 6, 1, 15, 17, 16, 14, 19, 2,300]

print(num)

def insert_sort(add_num):
    length = len(add_num)
    for i in range(0, length):
        x = add_num[i]
        for j in range(i,-1,-1):
            if add_num[j-1] > x:
                add_num[j] = add_num[j-1]
            else:
                break
        add_num[j] = x
    print(add_num)

insert_sort(num)