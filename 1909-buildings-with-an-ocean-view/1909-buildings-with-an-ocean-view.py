class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_right = [0]*len(heights)
        for i in range(len(heights)-2,-1,-1):
            max_right[i] = max(max_right[i+1], heights[i+1])
        # print(max_right)
        res = []
        for i in range(len(heights)):
            if heights[i]>max_right[i]:
                res.append(i)
        return res

