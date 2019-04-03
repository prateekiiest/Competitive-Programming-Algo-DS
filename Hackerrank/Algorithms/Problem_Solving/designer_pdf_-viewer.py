# Problem Statement : https://www.hackerrank.com/challenges/designer-pdf-viewer

#!/bin/python

import sys


h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()

width = len(word)
height = []
for i in word:
    p = h[ord(i) - 97]
    height.append(p)

r = max(height)

print(width*r)
