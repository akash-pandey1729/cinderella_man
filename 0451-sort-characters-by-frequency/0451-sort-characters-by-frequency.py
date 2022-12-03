class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        temp = [[key, c[key]] for key in c]
        temp.sort(key = lambda x:-x[1])
        ans = "".join([temp[i][0]*temp[i][1] for i in range(len(temp))])
        return ans
        