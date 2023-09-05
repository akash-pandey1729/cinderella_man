# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        ans =[]
        while stack:
            n = len(stack)
            ans.append([node.val for node in stack])
            for i in range(n):
                temp = stack.pop(0)
                if temp.left!=None:
                    stack.append(temp.left)
                if temp.right!=None:
                    stack.append(temp.right)
        return ans
