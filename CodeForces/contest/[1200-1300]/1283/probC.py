N = input()
A = map(int, raw_input().split())
 
V = [i + 1 for i in xrange(N) if A[i] == 0]
f = [1] * (N + 1)
for i in A: f[i] = 0
F = [i for i in range(1, N + 1) if f[i]]
 
n = len(F)
 
from random import shuffle as s
while 1:
    s(F)
    t = [i for i in xrange(n) if F[i] == V[i]]
    if not t:
        break
    
for i in xrange(n):
    A[V[i] - 1] = F[i]
for i in A: print i,