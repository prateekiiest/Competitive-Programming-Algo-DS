# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:37:52 2019

@author: pratik
"""


n = int(input())

reg = []

numbers = [str(k) for k in range(10)]
for i in range(n):
    st = raw_input()
    if st not in reg:
        reg.append(st)
        print("OK")
    else:
        id  = -1
        for item in range(len(reg)):
            if st in reg[item]:
                id = reg[item]
        num  = (id[-1])
        if num in numbers:
            q = int(num) + 1
            
            f = len(st)
            p =st[:f] + str(q)
            reg.append(p)
            
            
            print(p)
            
        else:
            
            f = len(st)
            p =st[:f] + "1"
            reg.append(p)
            
            
            print(p)       
