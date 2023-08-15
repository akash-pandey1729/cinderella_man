# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        gte = []
        less = []
        temp = head
        while head:
            if head.val>=x:
                gte.append(head.val)
            else:
                less.append(head.val)
            head = head.next
        head = temp
        ans = []
        ans.extend(less)
        ans.extend(gte)
        # print(ans)
        i = 0
        temp = head
        while head:
            head.val = ans[i]
            head = head.next
            i+=1
        return temp
            
        