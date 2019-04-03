# Problem Statement : https://www.hackerrank.com/challenges/equality-in-a-array

n = int(input())
A = list(map(int, raw_input().split()))

print ( n - max( [ A.count(t)  for t  in set(A) ]) )
