class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        nums1 = vec.nums
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for i in range(len(nums1)):
            dict1[i] = nums1[i]
        
        for i in range(len(self.nums)):
            dict2[i] = self.nums[i]
        
        ans = 0
        for key in dict1:
            if key in dict2:
                ans+= dict1[key]*dict2[key]
        return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)