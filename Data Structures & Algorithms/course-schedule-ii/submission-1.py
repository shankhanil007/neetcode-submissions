class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt
        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        hmap = {}
        for reqs in prerequisites:
            if not hmap.get(reqs[0], None):
                hmap[reqs[0]] = Node(reqs[1])
            else:
                head = hmap[reqs[0]]
                while head.nxt:
                    head = head.nxt
                head.nxt = Node(reqs[1])   

        ans = []

        def dfs(course, visited):
            visited.add(course)
            head = hmap.get(course, None)
            ret_val = True
            while head:
                if head.val not in visited:
                    ret_val = dfs(head.val, visited)
                else:
                    return False
                head = head.nxt
            if course not in ans:
                ans.append(course)
            visited.remove(course)
            return ret_val
        
        for course, prereqs in hmap.items():
            visited = set()
            if not dfs(course, visited):
                return []
        print(ans)
        for i in range(numCourses):
            if i not in ans:
                ans.append(i)
        return list(ans)
        
