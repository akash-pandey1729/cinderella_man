class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        poly_stack = []
        for i in range(len(s)):
            if s[i] == ')':
                if stack:
                    stack.pop()
                elif poly_stack:
                    poly_stack.pop()
                else:
                    return False
            elif s[i] == '(':
                stack.append(i)
            else:
                poly_stack.append(i)
        a = b = 0
        print(stack, poly_stack)
        while(a < len(stack) and b < len(poly_stack)):
            if stack[a] < poly_stack[b]:
                a += 1
                b += 1
            else:
                b += 1
        if (a == len(stack)):
            return True
        else:
            return False