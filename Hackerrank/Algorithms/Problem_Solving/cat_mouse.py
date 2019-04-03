# Problem Statement : https://www.hackerrank.com/challenges/cats-and-a-mouse

#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    
    catA = abs(x-z)
    catB = abs(y-z)
    
    if(catA== catB):
        print("Mouse C")
        
    elif(catA>catB):
        print("Cat B")
    
    elif(catB>catA):
        print("Cat A")
