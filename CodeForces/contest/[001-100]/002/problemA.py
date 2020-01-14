rounds = int(input())

names = []
scores = []
for case in range(rounds):
    arr = raw_input().split()
    
    names.append(arr[0])
    scores.append(int(arr[1]))
    