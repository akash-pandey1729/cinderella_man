"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def getRoot(node):
            if node.parent == None:
                return node
            return getRoot(node.parent)
        root = getRoot(p)

        def func(p,q,root):
            if not root:
                return None
            if root.val == q.val or root.val==p.val:
                return root
            left = func(p,q, root.left)
            right = func(p,q,root.right)

            if (left==q and right ==p) or (left==p and right==q):
                return root
            if not left:
                return right
            if not right:
                return left
        
        return func(p,q,root)
        