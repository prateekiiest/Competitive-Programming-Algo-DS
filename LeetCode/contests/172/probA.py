n = int(input())

str_num = list(str(n))

max_list = [n]    

str_len = len(str_num)
for k in range(str_len):
    if str_num[k] == '6':
        str_num[k] = '9'
        max_list.append(int(''.join(str_num)))
        str_num[k] = '6'
        
    else:
        
        str_num[k] = '6'
        max_list.append(int(''.join(str_num)))
        str_num[k] = '9'


print(max(max_list))