# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        diff = float('inf')
        res = []
        for i in range(len(ans)):
            if abs(ans[i]-target)<diff:
                res = []
                res.append(ans[i])
                diff = abs(ans[i]-target)
            elif abs(ans[i]-target)==diff:
                res.append(ans[i])
        res.sort()
        print(res)
        return res[0]


                


        