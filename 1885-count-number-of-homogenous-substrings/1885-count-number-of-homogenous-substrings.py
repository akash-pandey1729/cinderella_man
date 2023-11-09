class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        MOD = (10**9 + 7)
        streak = 1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                streak+=1
            else:
                streak = 1
            ans+= streak
        return (ans+1)%MOD
        