class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        def getHash(word1):
            shift = ord("z") - ord(word1[0]) + 1
            # print("shift", shift)
            res = []
            for i in range(len(word1)):
                res.append(str((ord(word1[i])+ shift)%26))
            return '-'.join(res)
        
        for word in strings:
            dict1[getHash(word)].append(word)
        return list(dict1.values())
        





        

        