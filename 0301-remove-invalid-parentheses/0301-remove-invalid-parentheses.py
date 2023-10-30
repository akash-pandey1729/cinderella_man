class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        max_length = 0

        def getMaxLength(s):
            arr = [0]*len(s)
            stack = []
            for i in range(len(s)):
                if s[i] == ')' and not stack:
                    arr[i] = -1
                elif s[i] == '(':
                    stack.append('(')
                elif s[i] == ')':
                    stack.pop()
            return arr.count(-1) + len(stack)
        t = getMaxLength(s)
        max_length = len(s)-t
        # print(t)
        ans = set()
        @lru_cache(None)
        def getUniqueStrings(s):
            if getMaxLength(s) == 0 and s not in ans:
                ans.add(s[:])
            for i in range(len(s)):
                temp = s[0:i] + s[i+1:]
                if len(temp)>=max_length:
                    getUniqueStrings(temp)
        getUniqueStrings(s)
        return list(ans)
            

        