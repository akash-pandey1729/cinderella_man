class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        dict1 = defaultdict(set)
        for cities in roads:
                dict1[cities[0]].add(cities[1])
                dict1[cities[1]].add(cities[0])
        cities = list(dict1.keys())
        max_degree = 0
        for i in cities:
            for j in cities:
                if i!=j:
                    if i in dict1[j]:
                        max_degree = max(max_degree, len(dict1[i]) + len(dict1[j])-1)
                    else:
                        max_degree = max(max_degree, len(dict1[i]) + len(dict1[j]))
        return max_degree
                
            
                    
                    
        
        