class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if stack and s[i]!= stack[-1][0]:
                stack.append([s[i], 1])
            elif stack and s[i] == stack[-1][0]:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([s[i], 1])
            
        ans = ""
        print("a"*3)
        print(stack)
        for ch, cnt in stack:
            ans+= ch*cnt
        return ans
            
        