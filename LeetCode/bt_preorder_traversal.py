# Submission Link : https://leetcode.com/submissions/detail/230198133/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


sol = []
class Solution(object):
   
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        self.preOrderList(root, res)
        return res
    
    def preOrderList(self,root,res):
	#check if root is not null 
        if root:
            res.append(root.val)
			
			
            self.preOrderList(root.left,res)
            self.preOrderList(root.right,res)
