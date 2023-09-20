class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)-1):
            if s[:i+1]*(len(s)//(i+1)) ==s:
                return True
        return False

        