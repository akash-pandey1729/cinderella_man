class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x:len(x))
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
        dp = [1]*len(words)
        for i in range(1, len(words)):
            for j in range(0,i):
                    if isChained(words[j],words[i]):
                        dp[i] = max(dp[i],dp[j]+1)
                    
        # print(dp)
        return max(dp)



        