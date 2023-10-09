class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def helper(p=0,q=0):
            if p>=len(nums1) or q>=len(nums2):
                return 0
            else:
                return  max(helper(p,q+1), helper(p+1,q), (nums1[p])*(nums2[q]) + helper(p+1,q+1)) 
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        return helper()


        