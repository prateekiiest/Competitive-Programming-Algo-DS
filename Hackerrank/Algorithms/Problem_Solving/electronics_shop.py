# Problem Statement : https://www.hackerrank.com/challenges/electronics-shop

#!/bin/python

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    l = []
    for k in keyboards:
        for r in drives:
            if(k+r <=s):
                l.append(k+r)
    
    if(l!=[]):
        return max(l)
    else:
        return -1
            

s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
