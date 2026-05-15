# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
            
        def isMirror(left, right):
            # If both are None, they are symmetric
            if not left and not right:
                return True
            # If one is None or values don't match, not symmetric
            if not left or not right or left.val != right.val:
                return False
            
            # Recursively check mirrors:
            # Outer pairs (left.left, right.right) and Inner pairs (left.right, right.left)
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
            
        return isMirror(root.left, root.right)