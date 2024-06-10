class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        ans=0
        for i in range(len(expected)):
            if expected[i]!=heights[i]:
                ans+=1
        return ans
        