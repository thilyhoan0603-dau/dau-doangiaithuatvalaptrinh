# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)   # Visit Left
            res.append(node.val)  # Visit Root
            traverse(node.right)  # Visit Right
            
        traverse(root)
        return res