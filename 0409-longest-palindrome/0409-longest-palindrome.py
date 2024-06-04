class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict1 = {}
        for i in s:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i]+=1
        ans = 0
        flag = False
        for i in dict1:
            if dict1[i]%2 ==0:
                ans = ans + dict1[i]
            else:
                flag = True
                ans = ans + (dict1[i]-1)
        if flag:
            return ans + 1
        return ans