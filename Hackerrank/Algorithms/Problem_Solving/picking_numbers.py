# Problem Statement : https://www.hackerrank.com/challenges/picking-numbers

#!/bin/python

import sys


n = int(raw_input().strip())
l = map(int,raw_input().strip().split(' '))


maximum=0
for i in l:
    c=l.count(i)
    d=l.count(i-1)
    c=c+d
    if c > maximum:
        maximum=c
print(maximum)
