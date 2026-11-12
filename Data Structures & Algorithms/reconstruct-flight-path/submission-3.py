class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = {}
        for source, dest in sorted(tickets, reverse=True):
            adj.setdefault(source, []).append(dest)

        stack = []
        stack.append("JFK")
        ans = []

        while stack:
            top = stack[-1]
            if not adj.get(top):
                ans.append(top)
                stack.pop()
            else:
                stack.append(adj[top].pop())

        ans.reverse()
        return ans 

