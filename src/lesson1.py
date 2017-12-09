#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def quadratic(a, b, c):
	for i in a, b, c:
		if not isinstance(i, (int, float)):
			raise TypeError('int or float')
			
	if a == 0:
		raise TypeError('error! a != 0')
		
	d = b ** 2 - 4 * a * c 
	if d < 0:
		return print('error')
	elif d >= 0:
		
		x1 = (-b + math.sqrt(d)) / (2 * a)
		x2 = (-b - math.sqrt(d)) / (2 * a)
		return x1, x2
	


if __name__ == '__main__':
    print(quadratic(2, 3, 1))
	#print(quadratic(1, 3, -4))

