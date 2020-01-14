import math
test = int(input())

for i in  range(test):
    n, d = map(int, raw_input().split(" "))
    
    if n >= d:
        print("YES")
    
    else:
        ite = 1
        res = "NO"
        while(ite < n):
            exp = ite + math.ceil(d/((ite+1)*1.0))
            #print(exp)
            if exp <= n:
                res = "YES"
                break
            else:
                ite += 1
        print(res)
        
        
        
        