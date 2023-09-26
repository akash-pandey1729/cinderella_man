class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        dict1 = Counter(s)
        for l in s:
            if l in stack:
                dict1[l]-=1
                continue
            while stack and dict1[stack[-1]]>1 and stack[-1]>=l:
                dict1[stack.pop()]-=1
            stack.append(l)
        return "".join(stack)


        