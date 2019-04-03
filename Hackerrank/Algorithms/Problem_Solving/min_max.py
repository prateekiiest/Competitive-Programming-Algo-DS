#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

z = min(sum([a,b,c,d]),sum([a,b,c,e]),sum([a,b,e,d]),sum([b,c,d,e]),sum([a,c,d,e]))
y = max(sum([a,b,c,d]),sum([a,b,c,e]),sum([a,b,e,d]),sum([b,c,d,e]),sum([a,c,d,e]))
print z, y


