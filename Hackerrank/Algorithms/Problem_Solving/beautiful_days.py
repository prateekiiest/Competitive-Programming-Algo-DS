# Problem Statement : https://www.hackerrank.com/challenges/beautiful-days-at-the-movies


# Enter your code here. Read input from STDIN. Print output to STDOUT
i,j,k = map(int, raw_input().split(" "))

def reverse(n):
    l = str(n)
    p = list(l)
    o = len(p) -1
    p.reverse()
        
    s = ''
    for g in p:
        s += g
    
    return int(s)
    

    
bea= 0    
for h in range(i,j+1):
    z = abs(h-reverse(h))
    if(z%k == 0):
        bea += 1
        
        
        
        
print(bea)
