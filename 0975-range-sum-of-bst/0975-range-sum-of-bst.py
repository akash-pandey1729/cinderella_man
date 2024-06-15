# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def func(root):
            if not root:
                return 0
            if root.val < low:
                return func(root.right)
            if root.val > high:
                return func(root.left)
            else:
                return root.val + func(root.right) + func(root.left)
        return func(root)
        



        