# Submission Link : https://leetcode.com/submissions/detail/231506799/

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            m = (left + right + 1) // 2
            if nums[m] == target:
                return m
            elif nums[m] <= nums[left] <= target or nums[left] <= target <= nums[m] or target <= nums[m] <= nums[left]:
                right = m - 1
            else:
                left = m + 1                
        return -1
