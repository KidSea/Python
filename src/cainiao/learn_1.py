#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys; x = 'runoob'; sys.stdout.write(x + '\n')

x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

for i in sys.argv:
    print(i)
print('\n Python 路徑为', sys.path)

a, b ,c , d = 20, 5.2, True, 5+3j

print(type(a), type(b), type(c), type(d))

print(isinstance(a, int))

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c += a
print("2 - c 的值为：", c)

c *= a
print("3 - c 的值为：", c)

c /= a
print("4 - c 的值为：", c)

c = 2
c %= a
print("5 - c 的值为：", c)

c **= a
print("6 - c 的值为：", c)

c //= a
print("7 - c 的值为：", c)

str = "nihao"
char  = 'g'

print(char in str)