class Solution:
    def specialArray(self, nums: List[int]) -> int:
        freq_arr = [0]*1001
        for i in range(len(nums)):
            freq_arr[nums[i]]+=1
        prefix_sum = [freq_arr[0]]
        
        for i in range(1, 1001):
            prefix_sum.append(prefix_sum[-1]+freq_arr[i])
        # print(prefix_sum)
        for i in range(1,len(prefix_sum)):
            if i==prefix_sum[-1]-prefix_sum[i-1]:
                print(i)
                return i
        return -1


        