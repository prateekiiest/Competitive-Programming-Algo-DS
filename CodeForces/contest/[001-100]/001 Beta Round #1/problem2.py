# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:35:31 2019

@author: pratik
"""

import string

numbers = [0,1,2,3,4,5,6,7,8,9]
alphabet = string.ascii_uppercase
alphabet  = list(alphabet)

str_num = [str(iu) for iu in numbers]
def check_type(num):
    
    
    out = "type2"
    for i in range(len(num)-1):
        if num[i+1] in alphabet and (num[i]) in str_num:
            out = "type1"
            break            

    return out
    
def convert(n):
	s = ''
	z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	
	while n>0:
		if n%26==0:
			n = n/26 - 1
			s+='Z'
		else:
			k = n%26
			n = n/26
			
			s+=z[k-1]
	
	return s[::-1]

    
    
def sconvert(s):
	z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	i = 0
	
	for l in s:
	
		k = z.index(l)+1
		i = i*26+k
		
	return i



n = int(input())




for i in range(n):
    num = raw_input()
    


    # type 1 : RXCY
    # type 2 : BC55  example

    ans = ""
    if check_type(num) == "type1":
        row = ""
        ind = -1
        for it in range(len(num)):
            if num[it] == "C":
                ind = it
                break
            
        row = num[1:ind]
        col = num[ind+1 :]
        s  = convert(int(col))
        ans  = s + row
        print(ans)
        
                
        
        
        
        
        
    else:
        ind = -1
        for it in range(len(num)):
            if (num[it]) in str_num:
                ind = it
                break
            
        row = num[ind:]
        col = num[:ind]
        
        s = sconvert(col)
        ans  =  "R" + row + "C" + str(s)
        
        
        print(ans)
