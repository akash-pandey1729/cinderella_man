class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjacency = [0 for i in range(len(edges) + 1)]
        for x,y in edges:
            adjacency[x-1]+=1
            adjacency[y-1]+=1
        _max = max(adjacency)
        for i in range(len(adjacency)):
            if adjacency[i] == _max:
                return i+1
        
        