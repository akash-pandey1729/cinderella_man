class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0]*n
        adjacency = defaultdict(list)
        for prev, nxt in relations:
            indegree[nxt-1]+=1
            adjacency[prev-1].append(nxt-1)

        time_sum = [time[i] for i in range(n)]
        def getTime(stack):
            while stack:
                temp = len(stack)
                for i in range(temp):
                    curr = stack.pop(0)
                    for nxt in adjacency[curr]:
                        time_sum[nxt] = max( time_sum[nxt], time_sum[curr]+ time[nxt])
                        indegree[nxt]-=1
                        if indegree[nxt]==0:
                            stack.append(nxt)
            return 
        stack = [i for i in range(len(indegree)) if indegree[i]==0]
        getTime(stack)
        return max(time_sum)






        