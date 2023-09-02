class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        dp = {}
        def func(i=0,j=len(s)):
            if s[i:j] in wordDict:
                dp[(i,j)] = True
                return True
            if (i,j) not in dp:
                dp[(i,j)] = False
                for k in range(i,j):
                    if func(i,k) and func(k,j):
                        dp[(i,j)] =  True
            return dp[(i,j)]
        return func()
        