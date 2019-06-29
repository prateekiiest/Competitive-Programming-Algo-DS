# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:30:30 2019

@author: pratik
"""

d, sumTime = raw_input().split()

d, sumTime = [int(d), int(sumTime)]

min_list = []
max_list = []
for i in range(d):
    min_t, max_t = raw_input().split()
    min_t, max_t = [int(min_t), int(max_t)]
    
    min_list.append(min_t)
    max_list.append(max_t)
    
    
    
if sumTime >= sum(min_list) and sumTime <= sum(max_list):
    print("YES")
    
else:
    print("NO")
