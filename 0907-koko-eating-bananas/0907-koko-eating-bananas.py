class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getHours(k):
            h = 0
            for pile in piles:
                if pile%k==0:
                    h+= pile//k
                else:
                    h+= 1+ pile//k
            return h
        print(getHours(24))
        left = 1
        right = max(piles)
        while left<right:
            mid = (left+right)//2
            if  getHours(mid)>h:
                left = mid+1
            else:
                right = mid
        return right

        


        