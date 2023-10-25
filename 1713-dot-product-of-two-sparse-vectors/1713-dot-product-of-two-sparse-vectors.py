class SparseVector:
    def __init__(self, nums: List[int]):
        self.list = nums
        self.dict1 = set()
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            else:
                self.dict1.add(i)
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for i in range(len(self.list)):
            if i in self.dict1 and i in vec.dict1:
                ans+= self.list[i]*vec.list[i]
        return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)