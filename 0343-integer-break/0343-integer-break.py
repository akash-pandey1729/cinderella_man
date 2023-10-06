class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2 or n==3:
            return n-1
        dict1 = {}
        def helper(n, parts):
            # print(n,parts)
            if n<2:
                return 0
            if parts==1:
                return n
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


        
        