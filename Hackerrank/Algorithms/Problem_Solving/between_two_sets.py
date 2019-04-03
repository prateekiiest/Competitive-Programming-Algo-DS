# Problem Statement : https://www.hackerrank.com/challenges/between-two-sets

#!/bin/python



import sys
from fractions import gcd

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
A = map(int,raw_input().strip().split(' '))
B = map(int,raw_input().strip().split(' '))

def LCM(a, b):
    return (a*b)//gcd(a,b)

lcm = reduce(LCM, A, 1)
gcd = reduce(gcd, B)

lcm_copy = lcm

count = 0
while lcm <= gcd:
    if(gcd % lcm) == 0:
        count += 1
    lcm = lcm + lcm_copy

print(count)

