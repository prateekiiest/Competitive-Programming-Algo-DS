# Problem Statement : https://www.hackerrank.com/challenges/find-digits

#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    s= list(str(n))
    c = 0
    for i in range(len(s)):
        s[i]= int(s[i])
     
    for j in s:
        if(j!=0 and n%j == 0):
            c+=1
          
    print(c)
            
