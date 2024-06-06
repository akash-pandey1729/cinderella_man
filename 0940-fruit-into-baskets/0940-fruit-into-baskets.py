class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        type_dict = defaultdict(int)
        left, ans = 0, 0
        for right in range(len(fruits)):
            type_dict[fruits[right]]+=1
            while len(type_dict)>2:
                type_dict[fruits[left]]-=1
                if type_dict[fruits[left]]==0:
                    del type_dict[fruits[left]]
                left+=1
            ans = max(ans, right-left + 1)
        return ans
        




        