class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t = 0
        while t<len(strs[0]):
            for i in range(1,len(strs)):
                if t>=len(strs[i]) or strs[i][t]!=strs[0][t]:
                    return strs[0][:t] if t!= 0 else ""
            t+=1
        return strs[0]
            
        