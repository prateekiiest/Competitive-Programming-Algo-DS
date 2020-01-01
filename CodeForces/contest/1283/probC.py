n = int(input())


arr = raw_input().split()
arr = [int(k) for k in arr]

output = [0 for i in range(n)]

for item in range(n):
    if arr[item] != 0:
        output[item] = arr[item] 
print(output)
