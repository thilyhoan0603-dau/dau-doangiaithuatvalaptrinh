# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Map values to indices for O(1) lookup
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        def array_to_tree(left, right):
            # If there are no elements to construct the tree
            if left > right:
                return None
            
            # Pick current root from preorder
            val = preorder.pop(0)
            root = TreeNode(val)
            
            # Root splits the inorder array into left and right subtrees
            idx = inorder_map[val]
            
            # Recursively build left and right subtrees
            root.left = array_to_tree(left, idx - 1)
            root.right = array_to_tree(idx + 1, right)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)