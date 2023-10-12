# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def getIndex(l,r):
            n = mountain_arr.length()
            while l<=r:
                mid=(l+r)>>1
                value=mountain_arr.get(mid)
                if (mid==0 or value>mountain_arr.get(mid-1)) and ((mid==n-1) or value>mountain_arr.get(mid+1)):
                    return mid
                elif value<mountain_arr.get(mid+1):
                    l=mid+1
                else:
                    r=mid-1
        
        def binSearchInc(lo,hi):
            while lo < hi:
                mid = (lo + hi) // 2
                # print(mid)

                if mountain_arr.get(mid) < target:
                    lo = mid + 1
                elif mountain_arr.get(mid) > target:
                    hi = mid
                elif mid > 0 and mountain_arr.get(mid-1) == target:
                    hi = mid
                else:
                    return mid

            return -1
        
        def binSearchDec(lo,hi):
            while lo < hi:
                mid = (lo + hi) // 2
                # print("dec",mid)

                if mountain_arr.get(mid) > target:
                    lo = mid + 1
                elif mountain_arr.get(mid) < target:
                    hi = mid
                elif mid > 0 and mountain_arr.get(mid-1) == target:
                    hi = mid
                else:
                    return mid

            return -1
        peak = getIndex(0,mountain_arr.length()-1)
        # print("peak", peak)
        # print("Increase",binSearchInc(0,peak))
        # print("decrease", binSearchDec(peak,mountain_arr.length()))
        if 0<=binSearchInc(0,peak+1)<= mountain_arr.length()-1 and mountain_arr.get(binSearchInc(0,peak+1)) == target:
            return binSearchInc(0,peak+1)
        if 0<=binSearchDec(peak,mountain_arr.length())<= mountain_arr.length()-1 and  mountain_arr.get(binSearchDec(peak+1,mountain_arr.length())) == target:
            return binSearchDec(peak,mountain_arr.length())
        # print(binSearchDec(peak+1,mountain_arr.length()-1))
        # print()
        return -1