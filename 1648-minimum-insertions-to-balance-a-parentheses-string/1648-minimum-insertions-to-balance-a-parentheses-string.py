class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace("))", "#")
        # three cases ch can be ( or # or (
        ans = 0
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(1)
            if ch == ")":
                if stack:
                    ans+=1
                    stack.pop()
                elif not stack:
                    # We need one open and one close bracket
                    ans+=2
            if ch == "#":
                if stack:
                    stack.pop()
                elif not stack:
                    # we need one open bracket
                    ans+=1
        ans += 2*(len(stack))
        return ans

        