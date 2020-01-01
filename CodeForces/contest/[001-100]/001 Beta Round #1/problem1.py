# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:27:08 2019

@author: pratik
"""

import math


n, m , a = raw_input().split()
n,m, a = [int(n), int(m) , int(a)]


row_wise = math.ceil(n/(a*1.0))
col_wise = math.ceil(m/(a*1.0))


ans = (row_wise * col_wise)

print(int(ans))

