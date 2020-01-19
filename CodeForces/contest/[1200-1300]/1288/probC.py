from math import factorial as fact

def C(n, k):
	return fact(n) // (fact(k) * fact(n - k))

n, m = map(int, input().split())
print(C(n + 2*m - 1, 2*m) % (10**9 + 7))