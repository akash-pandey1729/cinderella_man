class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        for key in cnt:
            ans+= cnt[key]*(cnt[key]-1)//2
        return ans + len(s)
        