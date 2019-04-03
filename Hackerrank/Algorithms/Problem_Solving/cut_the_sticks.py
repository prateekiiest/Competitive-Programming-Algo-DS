# Problem Statement : https://www.hackerrank.com/challenges/cut-the-sticks

#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

while(arr !=[]):
    print(len(arr))
    m = min(arr)
    for j in range(len(arr)):
        arr[j] -= m
    while(0 in arr):
        arr.remove(0)
    
    
            
        
