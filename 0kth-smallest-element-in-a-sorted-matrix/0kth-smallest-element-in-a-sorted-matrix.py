class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        for i in range(len(matrix)):
            for j in range(min(k,len(matrix[0]))):
                nums.append(matrix[i][j])
        nums.sort()
        for i in range(len(nums)):
            if i == k-1:
                return nums[i]
                
        
        
        