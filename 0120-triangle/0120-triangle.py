class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        def func(i=0,idx=0):
            if i==len(triangle):
                return 0
            if (i,idx) not in dp:
                if idx+1<len(triangle[i]):
                    dp[(i,idx)] = min(triangle[i][idx] + func(i+1, idx), triangle[i][idx+1]+ func(i+1, idx+1))
                else:
                    dp[(i,idx)] = triangle[i][idx] + func(i+1, idx)
            return dp[(i,idx)]
        return func()