# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        parent = defaultdict()
        parent[root] = root
        while stack:
            n = len(stack)
            stack_set = set(stack)
            for node in stack:
                if node.right in stack_set:
                    if parent[node].left==node:
                        parent[node].left = None
                        return root
                    else:
                        parent[node].right = None
                        return root
            for i in range(n):
                temp = stack.pop(0)
                if temp.left:
                    parent[temp.left] = temp
                    stack.append(temp.left)
                if temp.right:
                    parent[temp.right] = temp
                    stack.append(temp.right)
        return root

        