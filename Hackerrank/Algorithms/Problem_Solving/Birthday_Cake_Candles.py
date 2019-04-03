#!/bin/python

import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))

z = max(height)
co = 0
for j in range(n):
    if(height[j] == z ):
        co += 1

print(co)


