# Submission Link : https://leetcode.com/submissions/detail/230114741/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack != "":
            if needle not in haystack:
                return -1
            else:
                if needle != "":
                    return haystack.index(needle)
                else:
                    return 0
        else:
            if needle != "":
                return -1
            else:
                return 0
            
