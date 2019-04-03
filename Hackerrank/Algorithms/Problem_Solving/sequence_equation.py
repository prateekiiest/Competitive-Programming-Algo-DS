# Problem Statement : https://www.hackerrank.com/challenges/permutation-equation

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
p = map(int, raw_input().split(" "))

for i in range(1,n+1):
    for j in range(len(p)):
        if(i == p[j]):
            for k in range(n):
                if(j+1 == p[k]):
                    print(k+1)
        
