# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lcs(root):
            if not root:
                return None
            if root==p or root==q:
                return root
            left = lcs(root.left)
            right = lcs(root.right)
            if left and right:
                return root
            if left and not right:
                return left
            if not left and right:
                return right
            else:
                return None
                
        temp = lcs(root) 
        # if not node:
        #     return temp
        return temp
        