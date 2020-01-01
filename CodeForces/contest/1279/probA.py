test = int(input())

for i in range(test):
    arr = raw_input().split()
    arr = [int(k) for k in arr]
    #r,g,b = [int(arr[0]), int(arr[1]), int(arr[2])]
    arr  = sorted(arr)

    if((arr[2]) - (arr[1]) < 3):
        print("Yes")
    else:
        print("No")



