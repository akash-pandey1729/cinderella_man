class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for i in range(numCourses)]
        graph = {}
        for a,b in prerequisites:
            indegree[a]+=1
            if b not in graph:
                graph[b] = [a]
            else:
                graph[b].append(a)
        
        order = []
        stack = []
        for i in range(len(indegree)):
            if indegree[i]==0:
                stack.append(i)
        while stack:
            n = len(stack)
            for i in range(n):
                temp = stack.pop(0)
                order.append(temp)
                if temp in graph:
                    for course in graph[temp]:
                        indegree[course]-=1
                        if indegree[course]==0:
                            stack.append(course)
        return numCourses == len(order)

        