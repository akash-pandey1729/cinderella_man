class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        max_so_far = -1
        for i in range(len(heights)-1,-1,-1):
            if heights[i]>max_so_far:
                ans.append(i)
                max_so_far = heights[i]
        ans.sort()
        return ans
                


        