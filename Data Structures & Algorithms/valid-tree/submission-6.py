class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Build Adjacency List
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node, parent):

            visited.add(node)

            for neighbour in adj[node]:
                
                if neighbour == parent:      #### This should come first
                    continue
                
                if neighbour in visited:       #### This should be second
                    return True
                
                if dfs(neighbour, node):
                    return True
            return False

    
        # Check every component (handles disconnected graphs)
        if len(edges) + 1 != n:
            return False

        for i in range(n):
            if i not in visited:
                if dfs(i, -1):
                    return False

        return True