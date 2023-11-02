class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        all_tuples = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                    all_tuples.append((i+j, i, nums[i][j]))
        ans = []
        all_tuples.sort(key = lambda x:x[1], reverse = True)
        all_tuples.sort(key = lambda x:x[0])
        for t in all_tuples:
            ans.append(t[2])
        return ans
        
        