class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        adj = {i: [] for i in range(1, n+1)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        cycle = []
        self.start = -1

        def dfs(node, parent):
            visited.add(node)
            for nbr in adj[node]:
                if nbr == parent:
                    continue
                if nbr in visited:
                    self.start = nbr
                    cycle.append(node)
                    return True                #### IMP
                
                if dfs(nbr, node):
                    cycle.append(node)
                    if node == self.start:
                        return False
                    return True
            return False

        dfs(edges[0][0], -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        