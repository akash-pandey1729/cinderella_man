class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        def isEditDistanceOne(str1, str2):
            diff = 0
            for i in range(len(str1)):
                if str1[i]!=str2[i]:
                    diff+=1
            return diff == 1
        graph = defaultdict(list)
        for i in range(len(bank)):
            if isEditDistanceOne(bank[i], startGene):
                graph[startGene].append(bank[i])
            for j in range(i+1,len(bank)):
                if isEditDistanceOne(bank[i], bank[j]):
                    graph[bank[i]].append(bank[j])
                    graph[bank[j]].append(bank[i])
        visited = set()
        def getMinPath(startGene=startGene , cnt = 0):
            if startGene==endGene:
                return cnt
            min_cnt = float('inf')
            for gene in graph[startGene]:
                if startGene not in visited:
                    visited.add(startGene)
                    min_cnt = min(min_cnt, getMinPath(gene, cnt + 1))
                    visited.remove(startGene)
            return min_cnt
        temp = getMinPath()
        return temp if temp!=float('inf') else -1



 
    
        

        