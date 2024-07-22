class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = []
        for i in range(len(names)):
            ans.append([names[i], heights[i]])
        ans.sort(key = lambda x:x[1])
        res = []
        # print(ans)
        for i in range(len(ans)-1,-1,-1):
            res.append(ans[i][0])
        return res
        