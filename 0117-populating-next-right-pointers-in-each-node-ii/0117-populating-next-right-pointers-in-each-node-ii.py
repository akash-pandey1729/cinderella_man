"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = [root]
        while stack:
            n = len(stack)
            for i in range(n-1):
                stack[i].next = stack[i+1]
            for i in range(n):
                temp = stack.pop(0)
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
        return root
