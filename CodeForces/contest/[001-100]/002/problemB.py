n = int(input())

arr = []
for i in range(n):
    p = map(int, raw_input().split(" "))
    arr.append(p)
    
    
def no_zeroes(num):
    c = 0
    while(num % 10 == 0 ):
        num /= 10
        c += 1
        
        
    return c    

print(no_zeroes(2050000))
    