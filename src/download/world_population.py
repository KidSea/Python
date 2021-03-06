#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


# 将数据加载到一个列表中

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家2010年的人口数目
for pop_dict in  pop_data:
    if pop_dict['Year'] == '2010':
        contry_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        print(contry_name + ': ' + str(population))