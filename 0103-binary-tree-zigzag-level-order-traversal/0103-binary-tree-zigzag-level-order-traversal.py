# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        stack = [root]
        ans = []
        rev_flag = True
        while stack:
            n = len(stack)
            if not rev_flag:
                ans.append([node.val for node in list(reversed(stack))])
                rev_flag = True
            else:
                ans.append([node.val for node in stack])
                rev_flag = False
            for i in range(n):
                temp = stack.pop(0)
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
        return ans