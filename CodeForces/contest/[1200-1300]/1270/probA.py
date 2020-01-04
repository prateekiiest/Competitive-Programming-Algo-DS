test = int(input())

for case in range(test):
    n,k1,k2 = map(int,raw_input().split())
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())
    
    while(A!=[] or B !=[]):
        if A != []:
            best_a = max(A)
        else:
            break
        
        if B!=[]:
            best_b = max(B)
        else:
            break
        
        if best_a > best_b:
            B.remove(best_b)
            A.append(best_b)
        else:
            A.remove(best_a)
            B.append(best_a)
            
    if B == []:
        print("YES")
    else:
        print("NO")