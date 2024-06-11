class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        ans = []
        for num in arr2:
            ans.extend([num for i in range(cnt[num])])
            del cnt[num]
        rem = list(cnt.keys())
        rem.sort()
        for key in rem:
            ans.extend([key for i in range(cnt[key])])
        return ans


        


        