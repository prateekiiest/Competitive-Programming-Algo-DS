# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 20:10:00 2019

@author: pratik
"""

a,b,c,d = raw_input().split()

a,b,c,d = [int(a), int(b), int(c),int(d)]


from itertools import combinations



def check(tri):
    
    flag  = 0
    n = len(tri)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i !=j and j!= k:
                    if tri[i] + tri[j] >= tri[k]:
                        continue
                    else:
                        flag = 1
                        break
                    
    if flag == 1:
        return False
        
    else:
        return True
                    

l = [a,b,c,d]

count = 0
for item in combinations(l,3):
    if  check(item):
        count += 1
        
        
        
cnt = 0    
for item in combinations(l,3):
    cnt += 1

if count  ==  cnt  :
    print("TRIANGLE")
    
elif count >0 and count < cnt:
    print("SEGMENT")
    
elif count  == 0:
    print("IMPOSSIBLE")
