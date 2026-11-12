class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        par = [-1 for i in range(n + 1)]
        rank = [0] * (n + 1)

        def find(n):
            if par[n] == -1:
                return n
            par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            if rank[n1] > rank[n2]:
                par[n2] = n1
            elif rank[n2] > rank[n1]:
                par[n1] = n2
            else:
                par[n2] = n1
                rank[n1] += 1

        for n1, n2 in edges:
            source = find(n1)
            dest = find(n2)

            if source == dest:
                return [n1, n2]
            
            union(source, dest)
            