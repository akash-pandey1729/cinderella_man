# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head
        first = temp
        second = temp
        while second:
            if second.next and second.next.next:
                second = second.next.next
                first = first.next
            else:
                break
        return first.next
        
        