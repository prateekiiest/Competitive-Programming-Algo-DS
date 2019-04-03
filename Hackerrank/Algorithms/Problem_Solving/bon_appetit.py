# Problem Statement : https://www.hackerrank.com/challenges/bon-appetit

#!/bin/python

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    ar.remove(ar[k])
    s = sum(ar)
    ba = s/2
    if(b==ba):
        return('Bon Appetit')
    else:
        return abs(b-ba)

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
