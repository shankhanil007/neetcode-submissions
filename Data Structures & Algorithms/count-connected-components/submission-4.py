class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        ## Here cycle can exist and its okay with that 

        # Build Adjacency List
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for neighbour in adj[node]:

                if neighbour == parent:
                    continue
                
                if neighbour in visited:
                    continue                #### IMP
                
                dfs(neighbour, node)

    
        # Check every component (handles disconnected graphs)
        count = 0

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i, -1)


        return count