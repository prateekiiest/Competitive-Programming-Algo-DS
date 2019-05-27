# Submission Link: https://leetcode.com/submissions/detail/231266062/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root, flag=False):
        if root == None:  # if no node
            return 0
        if root.left == root.right == None and flag: # if leaf node
            return root.val
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)
