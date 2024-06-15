# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def visitNodes(node, high, low):
            nonlocal ans
            if not node:
                return 
            elif node.val<low:
                visitNodes(node.right, high, low)
            elif node.val>high:
                visitNodes(node.left, high, low)
            else:
                ans+= node.val
                visitNodes(node.left, high, low)
                visitNodes(node.right, high, low)
        visitNodes(root, high, low)
        return ans
        



        