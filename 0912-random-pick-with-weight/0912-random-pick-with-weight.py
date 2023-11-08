class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.range_arr = [() for i in w]
        # w.sort()
        self.range_arr[0] = (0,w[0]-1)
        for i in range(1, len(w)):
            self.range_arr[i] = (self.range_arr[i-1][1]+1,self.range_arr[i-1][1]+1+ w[i]-1)
        print(self.range_arr)
        self.sum_ = sum(w)

    def pickIndex(self) -> int:
        # check for boundaries
        # [0,2]
        r1 = random.randint(0, self.sum_-1)
        idx = bisect.bisect_left(self.range_arr,(r1,))
        if idx== len(self.range_arr) or r1<self.range_arr[idx][0]:
            idx-=1
        print(r1, idx)
        return idx

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()