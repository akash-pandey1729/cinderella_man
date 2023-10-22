"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal, None)
            head.next = head
            return head
        prev, curr = head, head.next
        while True:
            if prev.val<=insertVal and curr.val>= insertVal:
                prev.next = Node(insertVal, curr)
                return head
            if prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    prev.next = Node(insertVal, curr)
                    return head
            prev = prev.next
            curr = curr.next
            if curr==head:
                break
        prev.next = Node(insertVal, curr)
        return head
        





        