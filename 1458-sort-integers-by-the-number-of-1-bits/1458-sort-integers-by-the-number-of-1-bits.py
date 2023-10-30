class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        temp = [(arr[i], bin(arr[i])[2:]) for i in range(len(arr))]
        # print(temp)
        temp.sort(key = lambda x:x[0])
        temp.sort(key = lambda x: x[1].count('1'))
        return [temp[i][0] for i in range(len(temp))]

        