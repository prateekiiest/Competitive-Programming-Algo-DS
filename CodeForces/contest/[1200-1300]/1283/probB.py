test = int(input())

for case in range(test):
    arr = raw_input().split()
    n, k = [int(arr[0]), int(arr[1])]

    avg = n/(k*1.0)

    total = 0
    
    if n%k != 0:
        upper = int(avg) +1
        lower = int(avg)
    else:
        upper = int(avg)
        lower = int(avg)

    minimum_occur = int(k/(2.0))
    total += minimum_occur*upper 
    total += (k - minimum_occur)*lower

    if total <= n:
        print(total)
    else:
        print(n)


