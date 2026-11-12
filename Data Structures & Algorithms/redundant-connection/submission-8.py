class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        parent = [-1] * (n+1)
        rank = [0] * (n+1)

        def find(n):
            p = parent[n]
            if p == -1:
                return n
            parent[n] = find(parent[n])
            return parent[n]

        def union(n1, n2):
            if rank[n1] < rank[n2]:
                parent[n1] = n2
            elif rank[n2] > rank[n1]:
                parent[n1] = n2
            else:
                parent[n1] = n2
                rank[n2] += 1

        for u, v in edges:
            p1 = find(u)
            p2 = find(v)
            if p1 == p2:
                return [u, v]
            union(p1, p2)
