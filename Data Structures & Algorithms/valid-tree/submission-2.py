class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Build Adjacency List
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node: int, parent: int) -> bool:
            visited.add(node)

            for neighbor in adj[node]:
                # Ignore the edge we came from
                if neighbor == parent:
                    continue
                
                # If neighbor is already visited, a cycle exists!
                if neighbor in visited:
                    return True
                
                # Recursively check neighbor
                if dfs(neighbor, node):
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