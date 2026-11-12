class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = { i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)
        
        visited = set()
        processsed = []

        def dfs(course):

            visited.add(course)

            for reqs in adj[course]:
                if reqs in visited:
                    return True

                if reqs in processsed:
                    continue
                
                if dfs(reqs):
                    return True

            visited.remove(course)
            processsed.append(course)
            return False

        for course in range(numCourses):
            if course not in processsed and dfs(course):
                return []

        return processsed

        

        