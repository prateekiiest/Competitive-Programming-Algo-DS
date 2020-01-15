test = int(input())

for i in  range(test):
    A,B  = map(int, raw_input().split(" "))
    
    # first find for b
    
    len_b = len(str(B))
    nine_dig = ['9' for k in range(len_b)]
    nine_dig = ''.join(nine_dig)
    
    no_pairs_b = 0
    
    if B < int(nine_dig):
        no_pairs_b = (len(nine_dig) -1)*A
    elif B == int(nine_dig):
        no_pairs_b = (len(nine_dig))*A
    
    print(no_pairs_b)
    