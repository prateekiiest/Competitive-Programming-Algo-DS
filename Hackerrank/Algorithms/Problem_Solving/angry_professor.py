# Problem Statement : https://www.hackerrank.com/challenges/angry-professor

#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    p =0
    for j in a:
        if(j<=0):
            p +=1
    if(p<k):
        print('YES')
    elif(p>=k):
        print('NO')
