# Problem Statement : https://www.hackerrank.com/challenges/apple-and-orange

#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

# For apple
no_ap = 0
for i in range(len(apple)):
    z = a + apple[i]
    if(z>= s and z<=t):
        no_ap +=1
        
no_or = 0
for j in range(len(orange)):
    z = b + orange[j]
    if(z>= s and z<=t):
        no_or +=1
        
        
print(no_ap)
print(no_or)
        

