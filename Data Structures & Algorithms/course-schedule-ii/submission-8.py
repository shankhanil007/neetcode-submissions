
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # 1. Build Adjacency List: u -> list of courses that depend on u
        # prerequisites[i] = [a, b] means to take course 'a', you must first take 'b'
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        # State tracking: 0 = Unvisited, 1 = Visiting (current path), 2 = Visited (safe)
        state = [0] * numCourses
        ans = []

        def dfs(node: int) -> bool:
            # Base cases:
            if state[node] == 1:
                return True   # Cycle detected!
            if state[node] == 2:
                return False  # Already processed safely

            # Action: Mark as Visiting (on current path)
            state[node] = 1

            # Traverse prerequisites
            for prereq in adj[node]:
                if dfs(prereq):
                    return True

            # Backtrack: Mark as Visited (fully processed) and append to result
            state[node] = 2
            ans.append(node)
            return False

        # 2. Run DFS for every unvisited course
        for course in range(numCourses):
            if state[course] == 0:
                if dfs(course):
                    return []  # Return empty array if a cycle exists

        return ans