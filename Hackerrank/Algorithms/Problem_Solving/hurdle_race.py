# Problem Statement : https://www.hackerrank.com/challenges/the-hurdle-race

#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, raw_input().strip().split(' '))
# your code goes here
z = max(height)

if(k>=z):
    print(0)
else:
    print(z-k)
