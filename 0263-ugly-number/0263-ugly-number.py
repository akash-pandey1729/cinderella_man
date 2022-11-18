class Solution:
    def isUgly(self, n: int) -> bool:
        if n==1:
            return True
        if n%2!= 0 and n%5!=0 and n%3!=0 or n==0:
            return False
        val = self.isUgly(n/2) or self.isUgly(n/3) or self.isUgly(n/5)
        return val
        