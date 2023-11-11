# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, path):
            nonlocal ans
            if not root.left and not root.right:
                ans+= int( "".join(path + [str(root.val)]))
            elif not root.right and root.left:
                dfs(root.left, path + [str(root.val)])
            elif not root.left and root.right:
                dfs(root.right,path+[str(root.val)])
            else:
                dfs(root.left, path + [str(root.val)])
                dfs(root.right,path+[str(root.val)])

        dfs(root, [])
        return ans

        