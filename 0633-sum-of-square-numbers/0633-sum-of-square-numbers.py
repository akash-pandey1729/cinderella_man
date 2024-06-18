class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        while i*i<=c:
            temp = int(math.sqrt(c- i*i))
            if temp*temp == c- i*i:
                return True
            i+=1
        return False

        