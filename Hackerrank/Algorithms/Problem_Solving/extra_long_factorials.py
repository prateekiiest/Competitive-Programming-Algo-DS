# Problem Statement  : https://www.hackerrank.com/challenges/extra-long-factorials

#!/bin/python

import sys


n = int(raw_input().strip())

def fact(n):
    d = 1
    for i in range(1,n+1):
        d = d*i
        
    return long(d)

print(fact(n))
