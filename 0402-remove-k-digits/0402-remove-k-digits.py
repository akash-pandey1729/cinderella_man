class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = list(num)
        stack = []
        for i in range(len(num)):
            while k and stack and stack[-1]>num[i]:
                k-=1
                stack.pop()
            stack.append(num[i])
        finalStack = stack[:-k] if k else stack
        while finalStack and finalStack[0] == "0":
            finalStack.pop(0)
        return "".join(finalStack) if finalStack else "0"
            
            
        