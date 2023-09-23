class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dict1 = {}
        def isChained(w1, w2):
            if len(w1)!=len(w2)-1:
                return False
            else:
                i,j = 0,0
                while j<len(w2) and i<len(w1):
                    if w1[i] == w2[j]:
                        i+=1
                    j+=1
                return i==len(w1)
        def func(word):
            if len(word) == 1:
                return 1
            if word not in dict1:
                temp = 1
                for w in words:
                    if isChained(w,word):
                        temp = max(temp, func(w) +1)
                dict1[word] = temp
            return dict1[word]
        ans = 0
        for word in words:
            ans = max(ans, func(word))
        return ans



        