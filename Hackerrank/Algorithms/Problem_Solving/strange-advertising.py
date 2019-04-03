# Problem Statement : https://www.hackerrank.com/challenges/strange-advertising

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
        
z = 5
s = 0
i = 0
while(i<n):
    z = int(z/2)
    s += z
    z = z*3
    i += 1
    
print(s)
    
