# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    val = 0
    def bstToGst(self, root):
        if root.right: 
            self.bstToGst(root.right)
        root.val = self.val = self.val + root.val
        if root.left: 
            self.bstToGst(root.left)
        return root
