# Submission Link : https://leetcode.com/submissions/detail/230114086/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = (value for value in nums if value != val)
            
        return len(nums)
