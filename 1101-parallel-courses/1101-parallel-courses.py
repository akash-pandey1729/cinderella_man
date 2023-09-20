import copy
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        dict1 = {}
        indegree = [0 for i in range(n+1)]
        for prevCourse,nextCourse in relations:
            if prevCourse not in dict1:
                dict1[prevCourse] = [nextCourse]
            else:
                dict1[prevCourse].append(nextCourse)
            indegree[nextCourse]+=1
        stack = []
        stack_copy = []
        selections = []
        for i in range(n+1):
            if i!=0 and indegree[i]==0:
                if i in dict1:
                    stack.append(i)
                else:
                    selections.append(i)   
        t = 0
        while stack:
            t=t+1
            while stack:
                temp = stack.pop(0)
                if temp not in selections:
                    selections.append(temp)
                for i in dict1[temp]:
                    indegree[i]-=1
                    if indegree[i]==0:
                        if i in dict1:
                            stack_copy.append(i)
                        else:
                            selections.append(i)
            stack = copy.deepcopy(stack_copy)
            stack_copy = []
        return t+1 if len(selections)==n else -1
                
                    
                
            
        
        
                
        
            
            
            
        