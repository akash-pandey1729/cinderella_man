# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def makeTree(arr):
            if not arr:
                return None
            node = TreeNode(arr[len(arr)//2], makeTree(arr[0:len(arr)//2]), makeTree(arr[len(arr)//2+1:]))
            return node
        arr = []
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        # print(arr)
        if key in arr:
            arr.pop(arr.index(key))
            return makeTree(arr)
        else:
            return root



        