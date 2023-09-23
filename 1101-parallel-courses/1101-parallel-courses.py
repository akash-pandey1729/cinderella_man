import copy
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        dict1 = defaultdict(list)
        indegree = [0 for i in range(n)]
        for prevCourse,nextCourse in relations:
            dict1[prevCourse -1].append(nextCourse-1)
            indegree[nextCourse-1]+=1
        stack = []
        for i in range(n):
            if indegree[i] == 0:
                stack.append(i) 
        t = 0
        selections = set()
        while stack:
            t+=1
            l = len(stack)
            for i in range(l):
                course = stack.pop(0)
                selections.add(course)
                for c in dict1[course]:
                    indegree[c]-=1
                    if indegree[c]==0:
                        stack.append(c)
        return t if len(selections)==n else -1


        
                    
                
            
        
        
                
        
            
            
            
        