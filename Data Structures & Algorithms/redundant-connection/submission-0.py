class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(node, parent, visited):
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited:
                    return True                #### IMP
                
                if dfs(neighbour, node, visited):
                    return True
            return False


        adj = {}
        for edge in edges:
            u, v = edge[0], edge[1]

            # Initialize key if missing
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []

            # Safely append without re-assigning the result of .append()
            adj[u].append(v)
            adj[v].append(u)
            visited = set()
            if dfs(edge[0], -1, visited):
                return edge


        
    
      