"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_list = []
        def helper(head):
            if not head:
                return 
            temp = copy.deepcopy(head)
            temp.child = None
            node_list.append(temp)
            helper(head.child)
            helper(head.next)
            
        helper(head)

        for i in range(len(node_list)-1):
            node_list[i].next = node_list[i+1]
        
        for i in range(len(node_list)-1, 0,-1):
            node_list[i].prev = node_list[i-1]
        
        # for i in range(len(node_list)):
        #     node_list[i].child = None

        if not node_list:
            return None
        return node_list[0]







        