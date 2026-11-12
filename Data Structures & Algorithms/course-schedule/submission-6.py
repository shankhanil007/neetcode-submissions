class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i: [] for i in range(0, numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)

        visited = set()

        def dfs(node):

            visited.add(node)

            for reqs in adj[node]:
                if reqs in visited:
                    return True
                if dfs(reqs):
                    return True
            visited.remove(node)
            return False

        
        for course in range(0, numCourses):
            if course not in visited and dfs(course):
                return False
        return True


        