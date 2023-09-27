class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for l in s:
            if l.isdigit():
                size*=int(l)
            else:
                size+=1
        for l in reversed(s):
            k = k%size
            if k==0 and not l.isdigit():
                return l
            if l.isdigit():
                size = size/int(l)
            else:
                size-=1

        
        