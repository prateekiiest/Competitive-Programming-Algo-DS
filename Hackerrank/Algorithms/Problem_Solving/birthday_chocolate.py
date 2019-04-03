# Problem Statement : https://www.hackerrank.com/challenges/the-birthday-bar/problem

#!/bin/python

import sys

def solve(n, s, d, m):
    c = 0
    # Complete this function
    for i in range(n):
        if(sum(s[i:i+m]) == d):
            c += 1
    return c

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
