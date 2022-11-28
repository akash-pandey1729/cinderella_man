class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict1 = {}
        res = [[],[]]
        # print(dict1)
        for x,y in matches:
            if x not in dict1:
                dict1[x] = {"Win": 0, "Loss":0}
            if y not in dict1:
                dict1[y] = {"Win": 0, "Loss":0}
            dict1[x]["Win"]+=1
            dict1[y]["Loss"]+=1
        for key in dict1:
            if dict1[key]["Loss"] == 0 and dict1[key]["Win"]>0:
                res[0].append(key)
            if dict1[key]["Loss"] == 1:
                res[1].append(key)
        for item in res:
            item.sort()
        return res
            
            
            
        