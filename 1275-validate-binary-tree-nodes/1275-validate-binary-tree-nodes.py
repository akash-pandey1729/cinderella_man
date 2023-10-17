class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0 for i in range(n)]
        outdegree = [0 for i in range(n)]
        for i in range(n):
            if leftChild[i]==-1 and rightChild[i]==-1: 
                continue
            outdegree[i]+=1
            if leftChild[i]!=-1:
                indegree[leftChild[i]]+=1
            if rightChild[i]!=-1:
                indegree[rightChild[i]]+=1
        
        # print(indegree)
        # print(outdegree)
        # print()
        visited = set()
        def isCycle(node):
            if node == -1:
                return False
            if node in visited:
                return True
            visited.add(node)
            left = isCycle(leftChild[node])
            right = isCycle(rightChild[node])
            return left or right
        
        if 0 not in indegree:
            return False
        # for i in indegree:
        #     if i>1:
        #         return False
        # for i in outdegree:
        #     if i>2:
        #         return False

        if isCycle(indegree.index(0)):
            return False
        if len(visited)!=n:
            return False
        return True
            
        