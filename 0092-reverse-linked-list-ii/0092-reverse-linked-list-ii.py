# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        before = ListNode(0,head)
        right_node = None
        temp = head

        while temp and left>1:
            before = temp
            left-=1
            temp = temp.next

        temp = head
        while temp and right>0:
            right_node = temp
            right-=1
            if right==0:
                break
            temp = temp.next

        def reverseLinkedList(node):
            if not node.next:
                return node, node
            head, tail = reverseLinkedList(node.next)
            tail.next = node
            node.next = None
            return head, node
        # print(right_node.val, before.val)
        after_right = right_node.next
        right_node.next = None
        
        rev_head, rev_tail = reverseLinkedList(before.next)
        # print(
        # rev_head.val, rev_tail.val)
        before.next = rev_head
        rev_tail.next = after_right
        if rev_tail == head:
            return rev_head
        return head

        
        