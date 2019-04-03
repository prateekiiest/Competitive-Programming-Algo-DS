# Problem Statement : https://www.hackerrank.com/challenges/append-and-delete

#!/bin/python

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

for ops_left in reversed(range(1, k + 1)):
    if s == t[:len(s)] and len(t) - len(s) == ops_left or len(s) == 0:
        break
    s = s[:-1]
print "Yes" if len(t) - len(s) <= ops_left else "No"
