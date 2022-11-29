class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        dp  = {}
        def func(i=0,j=len(s)-1):
            if i>=j:
                return 0
            if (i,j) not in dp:
                if s[i] == s[j]:
                    dp[(i,j)] =  func(i+1,j-1)
                else:
                    dp[(i,j)] =  1+ min(func(i,j-1), func(i+1,j))
            return dp[(i,j)]
        return func()<=k
                
        