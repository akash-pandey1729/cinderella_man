# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        arr.sort()

        def getTree(arr):
            if not arr:
                return None
            root = TreeNode(arr[len(arr)//2], getTree(arr[:len(arr)//2]), getTree(arr[len(arr)//2+1:]))
            return root
        return getTree(arr)