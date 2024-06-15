class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        # print(path)
        res = []
        while path:
            temp = path.pop(0)
            if res and temp== "..":
                res.pop()
            if temp == "" or temp == " " or temp =="." or temp == "..":
                continue
            else:
                res.append(temp)
        
        return "/"+ "/".join(res)


       
        