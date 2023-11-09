class Solution:
    def countHomogenous(self, s: str) -> int:
        l,r = 0,0
        ans = 0
        while r<len(s):
            # print(r,l)
            if s[l]!=s[r]:
                ans+= (r-l)*(r-l+1)//2
                l=r
            r+=1
        print(r,l, "here")
        ans+=(r-l)*(r-l+1)//2
        return ans%(10**9 + 7)
                

        