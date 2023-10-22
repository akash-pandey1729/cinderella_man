class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        prefix_kadane = [-float('inf')]*len(arr)
        suffix_kadane = [-float('inf')]*len(arr)
        prefix_kadane[0] = arr[0]
        suffix_kadane[-1] = arr[-1]
        for i in range(1, len(arr)):
            prefix_kadane[i] = max(prefix_kadane[i-1]+ arr[i], arr[i])

        for i in range(len(arr)-2,-1,-1):
            suffix_kadane[i] = max(suffix_kadane[i+1]+ arr[i], arr[i])
        # print(prefix_kadane)
        # print(suffix_kadane)
        ans = -float('inf')
        for i in range(1,len(arr)-1):
            ans = max(ans, suffix_kadane[i+1]+ prefix_kadane[i-1])
        return max(ans, max(prefix_kadane))

        