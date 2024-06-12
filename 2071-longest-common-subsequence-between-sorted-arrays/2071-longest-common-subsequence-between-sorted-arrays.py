class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        big_dict = defaultdict(dict)
        big_set = set()
        for i in range(len(arrays)):
            big_dict[i] = Counter(arrays[i])
            for key in big_dict[i]:
                big_set.add(key)
        common = defaultdict(int)
        # print(big_set)
        # print(big_dict)
        for num in big_set:
            if num not in common:
                common[num] = 1
            for key in big_dict:
                if num not in big_dict[key]:
                    common[num] = -1*float('inf')
                else:
                    common[num] = min(common[num], big_dict[key][num])
        lcs = []
        # print(common)
        for key in common:
            if common[key]!= -1*float('inf'):
                lcs.extend([key for i in range(common[key])])
        lcs.sort()
        return lcs






                
        