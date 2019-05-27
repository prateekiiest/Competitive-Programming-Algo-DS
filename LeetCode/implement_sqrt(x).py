# Problem Link : https://leetcode.com/submissions/detail/231655123/

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while(i<x):
            if i*i > x:
                break
            i += 1
        if x == 0:
            return 0
        if x == 1:
            return 1
        else:
            return i-1
