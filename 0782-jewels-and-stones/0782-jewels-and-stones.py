class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = Counter(stones)
        ans = 0
        for i in jewels:
            ans+= cnt[i]
        return ans
        