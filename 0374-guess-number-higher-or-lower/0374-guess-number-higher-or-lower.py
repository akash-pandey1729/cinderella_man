# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def func(l,h):
            if l<=h:   
                m = (l+h)//2
                if guess(m)==0:
                    return m
                if guess(m) == -1:
                    h = m-1
                    return func(l,h)
                else:
                    l = m+1
                    return func(l,h)
        return func(1,n)
        