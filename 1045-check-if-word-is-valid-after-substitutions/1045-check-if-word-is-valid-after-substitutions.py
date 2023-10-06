class Solution:
    def isValid(self, s: str) -> bool:
        # print(s.replace("abc", ""))
        while "abc" in s:
            s = s.replace("abc", "")
        return s==""
        