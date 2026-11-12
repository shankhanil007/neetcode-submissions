class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1:
            return False

        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def helper(curr_node, prt):

            visited.add(curr_node)

            for nbr in adj[curr_node]:

                if nbr == prt:
                    continue

                if nbr in visited:
                    return True
                
                if helper(nbr, curr_node):
                    return True

            return False

        for i in range(n):
            if i not in visited:
                if helper(i, -1):
                    return False

        return True
