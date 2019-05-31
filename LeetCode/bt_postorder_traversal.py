# Submission Link : https://leetcode.com/submissions/detail/230198455/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
   
        res=[]
        self.postOrderList(root, res)
        return res
    
    def postOrderList(self,root,res):
	#check if root is not null 
        if root:
			
			
            self.postOrderList(root.left,res)
            self.postOrderList(root.right,res)
            res.append(root.val)
