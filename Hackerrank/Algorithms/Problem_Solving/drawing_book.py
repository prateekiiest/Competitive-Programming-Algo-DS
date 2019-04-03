# Problem Statement : https://www.hackerrank.com/challenges/drawing-book

#!/bin/python

import sys

def solve(n, p):
    # Complete this function
    
    z = min((p/2),(n/2-p/2))
    return z
n = int(raw_input().strip())
p = int(raw_input().strip())
result = solve(n, p)
print(result)
