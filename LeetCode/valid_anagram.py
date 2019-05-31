# Submission Link : https://leetcode.com/submissions/detail/230781316/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False
        
