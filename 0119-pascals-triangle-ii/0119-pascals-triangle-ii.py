class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def getRow(r):
            if r==0:
                return [1]
            if r==1:
                return [1,1]
            else:
                ans = []
                temp = getRow(r-1)
                for i in range(len(temp)-1):
                    ans.append(temp[i]+temp[i+1])
                ans.append(1)
                ans.insert(0,1)
                return ans
        return getRow(rowIndex)
        