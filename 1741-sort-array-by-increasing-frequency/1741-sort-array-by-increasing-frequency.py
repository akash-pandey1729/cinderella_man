class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i]+=1
        # print(dict1)
        ans = []
        for i in dict1:
            ans.append([dict1[i],i])
        # print(ans)
        ans.sort(key = lambda x:x[1], reverse = True)
        ans.sort(key = lambda x:x[0])
        ret = []
        for i in ans:
            ret.extend([i[1] for j in range(i[0])])
        return ret
        