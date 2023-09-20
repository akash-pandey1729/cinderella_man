class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def IsNice(s):
            return len(set(s.lower())) == (len(set(s)) // 2)
        ans = 0
        # print(IsNice("Bb"))
        temp = ""
        for i in range(len(s)+1):
            for j in range(i+1,len(s)+1):
                if IsNice(s[i:j]) and ans<j-i + 1:
                    ans = max(ans, j-i + 1)
                    temp = s[i:j]
        return temp 
