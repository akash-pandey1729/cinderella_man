class Solution:
    def integerBreak(self, n: int) -> int:
        dict1 = {}
        def helper(n, parts):
            # print(n,parts)
            if parts==n:
                return 1
            if (n, parts) not in dict1:
                ans = 0
                for part in range(2,n+1):
                    ans = max(ans, part*helper(n-part, parts-1))
                dict1[(n,parts)] = ans
            return dict1[(n,parts)]
        res = 0
        for i in range(2,n+1):
            res = max(res, helper(n,i))
        return res


        
        