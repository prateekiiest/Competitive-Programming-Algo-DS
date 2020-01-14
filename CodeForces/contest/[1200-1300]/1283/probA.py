test = int(input())

for case in range(test):
    arr = raw_input().split()
    hour, mins = [int(arr[0]), int(arr[1])]
    output = 0
    if hour == 0 and mins == 0:
        output = 0

    else:
        total = 0
        total += (23 - hour)*60
        total += (60 - mins)
        output = total

    print(output)

