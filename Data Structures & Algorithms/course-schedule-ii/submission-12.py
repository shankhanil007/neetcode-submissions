class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {i: [] for i in range(0, numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)

        visited = set()
        processed = []

        def dfs(node):

            visited.add(node)

            for reqs in adj[node]:
                if reqs in visited:
                    return True

                elif reqs in processed:   
                    continue

                if dfs(reqs):
                    return True
            
            processed.append(node)
            visited.remove(node)
            return False

        
        for course in range(0, numCourses):
            if course not in processed and dfs(course):  #### IMP not in processed NOT visited. Visited becomes empty after every traversal. So it will run DFs for every course
                return []
        return processed


        