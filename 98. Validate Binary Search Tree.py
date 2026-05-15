# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validate(node, low, high):
            # An empty tree is a valid BST
            if not node:
                return True
            
            # The current node's value must be strictly between low and high
            if not (low < node.val < high):
                return False
            
            # Recursively check the subtrees with updated constraints
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        # Use float('-inf') and float('inf') for the initial boundaries
        return validate(root, float('-inf'), float('inf'))