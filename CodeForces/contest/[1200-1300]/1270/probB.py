test = int(input())

for case in range(test):
    n = int(input())
    arr = map(int, raw_input().split())
    
    
    l = -1
    r = -1
    for i in range(n-1):
        if arr[i+1] - arr[i] >=2:
            l = i
            r = i+1
            break 
    
    if l == -1:
        print("NO")
    else:
        print("YES")
        print(str(l) + " "+ str(r))