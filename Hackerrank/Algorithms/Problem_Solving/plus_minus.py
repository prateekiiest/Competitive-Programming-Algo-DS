#!/bin/python


from __future__ import division
import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))


positive = 0
negative =0
zero = 0
for i in range(n):
    if(arr[i] > 0):
        positive += 1
    elif(arr[i] < 0):
        negative += 1
      
    else:
        zero += 1
        
pos = (positive/n)
neg = (negative/n)
z = (zero/n)

print(pos)
print(neg)
print(z)
