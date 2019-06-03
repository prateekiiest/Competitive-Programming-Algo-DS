class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            s = list(str(x))
            l  = 0
            for k in range(len(s)):
                if s[k] == s[len(s)-k-1]:
                    l += 1
            
            if l == len(s):
                return True
            else:
                return False
