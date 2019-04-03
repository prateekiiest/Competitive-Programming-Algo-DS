# Problem Statement : https://www.hackerrank.com/challenges/breaking-best-and-worst-records


#!/bin/python

import sys

def getRecord(scores):
    ls = hs = s[0];
    lc = hc = 0;
    
    for score in scores:
        if(score > hs):
            hs = score;
            hc += 1;
        
        if(score < ls):
            ls = score;
            lc += 1;
            
    return [hc, lc]
        

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
