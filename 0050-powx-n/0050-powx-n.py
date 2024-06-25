class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def func(x,n):
            if n==0:
                return 1
            else:
                if n%2: #n is odd
                    t = func(x,n//2)
                    return x*t*t
                else:
                    t = func(x,n//2)
                    return t*t
        if n<0:
            ans = func(x,abs(n))
            return 1/ans
        else:
            return func(x,abs(n))