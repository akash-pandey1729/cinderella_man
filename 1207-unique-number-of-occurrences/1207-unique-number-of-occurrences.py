class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c= Counter(arr)
        dict1 = set()
        for key in c:
            if c[key] not in dict1:
                dict1.add(c[key])
            else:
                return False
        return True
        