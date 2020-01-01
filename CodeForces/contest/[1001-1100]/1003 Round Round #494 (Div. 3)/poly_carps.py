t= int(input())

arr = raw_input().split()

arr  = [int(k) for k in arr]


freq = {}
for item in arr:
	if item in freq:
		freq[item] += 1
	else:
		freq[item] = 1
		
	

maxim = 0
for it in freq:
	if freq[it] >= maxim:
		maxim = freq[it]
		
print(maxim)
		
