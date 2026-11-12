class DSU:
    def __init__(self, n):
        self.num_nodes = n
        self.parent = [-1] * n
        self.rank = [0] * n
        
    def find(self, node):
        if self.parent[node] == -1:
                return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        if self.rank[node1] < self.rank[node2]:
            self.parent[node1] = node2
        elif self.rank[node1] > self.rank[node2]:
            self.parent[node2] = node1
        else:
            self.parent[node1] = node2
            self.rank[node2] += 1















class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    
        n = len(edges)
        dsu = DSU(n+1)        

        
        for u, v in edges:
            prt1 = dsu.find(u)
            prt2 = dsu.find(v)
            if prt1 == prt2: 
                return [u, v]
            dsu.union(prt1, prt2)   ### union of prnts
        