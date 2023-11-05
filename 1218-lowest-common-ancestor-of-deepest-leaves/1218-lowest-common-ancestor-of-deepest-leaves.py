# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dict1 = defaultdict(int)
        def getDepth(node):
            if not node:
                return 0
            dict1[node] = 1 + max(getDepth(node.left), getDepth(node.right))
            return dict1[node] 

        getDepth(root)

        def getCommonNode(root):
            if dict1[root.left] == dict1[root.right]:
                return root
            if dict1[root.left]> dict1[root.right]:
                return getCommonNode(root.left)
            return getCommonNode(root.right)

        return getCommonNode(root)
             
            
            
        