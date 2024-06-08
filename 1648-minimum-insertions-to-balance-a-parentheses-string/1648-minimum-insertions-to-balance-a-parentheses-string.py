class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace("))", "#")
        # three cases
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
                    ans+=2
            if ch == "#":
                if stack:
                    stack.pop()
                elif not stack:
                    ans+=1
        ans += 2*(len(stack))
        return ans

        