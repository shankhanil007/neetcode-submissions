
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {i: [] for i in range(0, numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)

        visited = set()
        ans = []

        def dfs(node):
            visited.add(node)
            for reqs in adj[node]:
                if reqs in visited and reqs not in ans:
                    return True
                elif reqs in ans:
                    continue
                elif dfs(reqs):
                    return True
            visited.remove(node)
            ans.append(node)
            return False

        
        for course in range(0, numCourses):
            if course not in ans and dfs(course):
                return []
        return ans
