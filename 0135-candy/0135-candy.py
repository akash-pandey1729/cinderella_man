class Solution:
    def candy(self, ratings: List[int]) -> int:
        leftToRight = [1 for i in range(len(ratings))]
        rightToLeft = [1 for i in range(len(ratings))]
        for i in range(len(ratings)-1):
            if ratings[i+1]>ratings[i]:
                leftToRight[i+1] = leftToRight[i]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                rightToLeft[i] = rightToLeft[i+1]+1
        ans = 0
        for i in range(len(ratings)):
            ans+= max(rightToLeft[i], leftToRight[i])
        return ans
            
        