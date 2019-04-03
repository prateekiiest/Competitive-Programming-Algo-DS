# Problem Statement : https://www.hackerrank.com/challenges/sock-merchant

#!/bin/python

import sys

def sockMerchant(n, ar):
    # Complete this function
    s = list(set(ar))
    c =0 
    for j in s:
                   
        z = ar.count(j)
        c += int(z/2)
    return c
            

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = sockMerchant(n, ar)
print(result)
