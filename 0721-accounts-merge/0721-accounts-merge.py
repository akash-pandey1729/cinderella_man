class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        id_ = 0
        email_name_map = defaultdict()
        for account in accounts:
            for i in range(1,len(account)):
                graph[account[i]] =  graph[account[i]].union(set(account[1:]))
                graph[account[i]].remove(account[i])
                email_name_map[account[i]] = account[0]
        # print(graph)
        def dfs(email,visited):
            for neighbor in graph[email]:
                if neighbor not in visited:
                    big_visited.add(neighbor)
                    visited.add(neighbor)
                    dfs(neighbor,visited)
        ans = []
        big_visited = set()
        for email in graph.keys():
            if email not in big_visited:
                big_visited.add(email)
                visited = set()
                visited.add(email)
                big_visited.add(email)
                dfs(email, visited)
                temp = [email_name_map[email]]
                visited = list(visited)
                visited.sort()
                temp.extend(visited)
                ans.append(temp)
        return ans




        
        
        
        