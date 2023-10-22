class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_list = set()
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack and s[i]==')':
                stack.pop()
            elif not stack and s[i]==')':
                index_list.add(i)
        ans = ""
        # print(index_list)
        # print(stack)
        index_list = index_list.union(set(stack))
        for i in range(len(s)):
            if i in index_list:
                continue
            ans+=s[i]
        return ans

        