# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0, float('inf'), -float('inf')

        left_cnt, left_min, left_max = self.help(root.left)
        right_cnt, right_min, right_max = self.help(root.right)

        if left_cnt is not -1 and right_cnt is not -1 and left_max < root.val and  root.val < right_min:
            self.result = max(self.result, left_cnt + 1 + right_cnt)
            return left_cnt + 1 + right_cnt, min(left_min, root.val, right_min), max(left_max, root.val, right_max)
        
        return -1, -1, -1 # subtree is not a BST

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.help(root)
        return self.result