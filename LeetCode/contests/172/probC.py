# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if (root == None): 
            return None
        
        root.left = self.removeLeafNodes(root.left, target)  
        root.right = self.removeLeafNodes(root.right, target)  
  
        if (root.val == target and 
           self.isnode_Leaf(root)): 
            return None # replace with Null. Delete the node
        
        return root 
    
    
    
    def isnode_Leaf(self, root):
        if root.left ==  None and root.right == None:
            return True
        else:
            return False