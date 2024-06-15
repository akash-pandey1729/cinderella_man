class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        i = 0
        while i<len(path):
            if path[i] == "/":
                ans.append("/")
                i+=1
                while i<len(path) and path[i] == "/":
                    i+=1
            else:
                ans.append(path[i])
                i+=1
        s = "".join(ans)
        s= s.split("/")
        # print(s)
        res = []
        while s:
            temp = s.pop(0)
            if temp == "" or temp == " " or temp ==".":
                continue
            if res and temp== "..":
                res.pop()
            else:
                if temp!="..":
                    res.append(temp)
        
        return "/"+ "/".join(res)


       
        