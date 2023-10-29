class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        temp = [(abs(arr[i]-x), i) for i in range(len(arr))]
        # print(temp)
        temp.sort(key = lambda x:x[1])
        temp.sort(key = lambda x:x[0])
        # print(temp)
        ans = []
        while k>0:
            ans.append(arr[temp.pop(0)[1]])
            k-=1
        ans.sort()
        return ans



        