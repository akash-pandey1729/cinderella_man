class Solution:
    def hammingWeight(self, n: int) -> int:
        def decToBin(n):
            if n==0:
                return ''
            else:
                return decToBin(n//2) + str(n%2)
        print(n)
        n = decToBin(n)
        print(n)
        ans = 0
        for i in n:
            if i=='1':
                ans = ans + 1
        return ans
        