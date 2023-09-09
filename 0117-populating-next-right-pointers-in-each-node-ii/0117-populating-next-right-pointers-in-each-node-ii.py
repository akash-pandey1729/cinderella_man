class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        stack = []
        stack.append(root)
        dummy=Node(-999) # to initialize with a not null prev
        while stack:
            length=len(stack) # find level length
            prev=dummy
            for _ in range(length): # iterate through all nodes in the same level
                popped=stack.pop(0)
                if popped.left:
                    stack.append(popped.left)
                    prev.next=popped.left
                    prev=prev.next
                if popped.right:
                    stack.append(popped.right)
                    prev.next=popped.right
                    prev=prev.next                 
        return root