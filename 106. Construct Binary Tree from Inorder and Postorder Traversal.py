# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # Map values to indices for O(1) lookup
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(in_left, in_right):
            # If there are no elements to construct the tree
            if in_left > in_right:
                return None
            
            # The last element in postorder is the current root
            val = postorder.pop()
            root = TreeNode(val)
            
            # Find the split point in inorder
            index = idx_map[val]
            
            # Build right subtree then left subtree
            # (Because we are popping from the end of postorder)
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            
            return root
            
        return helper(0, len(inorder) - 1)