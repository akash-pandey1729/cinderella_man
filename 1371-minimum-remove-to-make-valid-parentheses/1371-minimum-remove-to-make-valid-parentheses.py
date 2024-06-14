class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        bad = []
        for i in range(len(s)):
            if s[i].isalpha():
                continue
            elif s[i]=="(":
                stack.append(i)
            elif s[i]==")" and len(stack)>0:
                stack.pop()
            elif s[i]==")" and len(stack)==0:
                bad.append(i)
        res = []
        stack = set(stack)
        bad = set(bad)
        for i in range(len(s)):
            if i in stack or i in bad:
                continue
            res.append(s[i])
        return "".join(res)
            
        