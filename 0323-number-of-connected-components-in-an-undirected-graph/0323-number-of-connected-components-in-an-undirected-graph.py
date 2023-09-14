class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
    
        def union(x,y):
            if parent[x]!=parent[y]:
                pX = find(x)
                pY = find(y)
                if pX!=pY:
                    if rank[pX]<rank[pY]:
                        parent[pX] = pY
                    elif rank[pX]>rank[pY]:
                        parent[pY] = pX  
                    else:
                        parent[pY] = pX
                        rank[pX]+=1
        for x,y in edges:
            union(x,y)
        print(parent)
        for i in range(n):
            find(i)
        return len(set(parent))
