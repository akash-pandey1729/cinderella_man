class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def getNumFromBin(a):
            ans = 0
            t = 0
            for i in range(len(a)-1,-1,-1):
                ans+= int(a[i])*(2**t)
                t+=1
            return ans
        return bin(getNumFromBin(a) + getNumFromBin(b))[2:]

        
        