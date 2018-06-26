#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数

import sys

a, b = 0, 1

while b < 1000:
    print(b)
    a, b = b, a + b

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

def paixu(data):
    max = 0
    for i in range(len(data) - 1):
        for j in range(len(data) - i -1):
            if data[j] > data[j + 1]:
                max = data[j]
                data[j] = data[j + 1]
                data[j + 1] = max
            else:
                max = data[j + 1]
    print(data)

paixu([41,23344,9353,5554,44,7557,6434,500,2000])

f = fibonacci(10)q

print(next(f))

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()