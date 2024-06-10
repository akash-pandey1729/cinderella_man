class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = []
        for x,y in paths:
            cities.append(x)
            cities.append(y)
        cnt = Counter(cities)
        for x,y in paths:
            if cnt[y]==1:
                return y

        