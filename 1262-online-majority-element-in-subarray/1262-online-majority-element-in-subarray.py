class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.dict1 = defaultdict(list)
        for i in range(len(arr)):
            self.dict1[arr[i]].append(i)
        

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            a = self.arr[random.randint(left, right)]
            l = bisect.bisect_left(self.dict1[a], left)
            r = bisect.bisect_right(self.dict1[a], right)
            if r - l >= threshold:
                return a
        return -1



# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)