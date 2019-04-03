# Problem Statement :  https://www.hackerrank.com/challenges/utopian-tree


#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    #h= 1
    if(n==0):
        print(1)
    
    elif(n==1):
        print(2)
    
    elif(n%2==0):
        h = 1
        for j in range(n/2):
           
            h *= 2
            h += 1
        print(h)
        
    elif(n%2 !=0):
        z = n - 1
        h = 1
        for j in range(z/2):
            
            h= h*2
            h += 1
        h *=2
        print(h)
            
