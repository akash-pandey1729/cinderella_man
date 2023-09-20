class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjacency = defaultdict(list)
        nodes = set()
        for x,y in edges:
            nodes.add(x)
            nodes.add(y)
            adjacency[x].append(y)
            adjacency[y].append(x)
        for key in adjacency.keys():
            if len(adjacency[key]) == len(nodes)-1:
                return key
        
        