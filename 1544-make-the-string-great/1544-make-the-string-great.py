class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        ans = []
        for i in range(len(s)):
            if ans and s[i].islower() and ans[-1].islower():
                ans.append(s[i])
            elif ans and s[i].isupper() and ans[-1].isupper():
                ans.append(s[i])
            elif ans and (s[i].lower() == ans[-1] or s[i].upper() == ans[-1]):
                ans.pop()
            else:
                ans.append(s[i])
        return "".join(ans)
            
            
        