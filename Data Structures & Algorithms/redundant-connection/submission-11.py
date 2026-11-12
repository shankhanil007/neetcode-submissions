class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

        n = len(edges)
        parent = [-1] * (n+1)
        rank = [0] * (n+1)

        def find(node):
            if parent[node] == -1:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            if rank[node1] < rank[node2]:
                parent[node1] = node2
            elif rank[node1] > rank[node2]:
                parent[node2] = node1
            else:
                parent[node1] = node2
                rank[node2] += 1

        
        for u, v in edges:
            prt1 = find(u)
            prt2 = find(v)
            if prt1 == prt2:
                return [u, v]
            union(prt1, prt2)   ### union of prnts
        