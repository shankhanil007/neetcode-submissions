class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        pacific = set()
        atlantic = set()
        nrows = len(heights)
        ncols = len(heights[0])
        
        dx = [0, -1, 1, 0]
        dy = [-1, 0, 0, 1]

        def bfs(i, j, ocean):
            queue = collections.deque()
            visited = [[False]*ncols for _ in range(nrows)]
            queue.append((i, j))
            visited[i][j] = True
            ocean.add((i,j))

            while queue:
                top = queue.popleft()
                curr_row = top[0]
                curr_col = top[1]
                for itr in range(0, 4):
                    new_row = curr_row + dx[itr]
                    new_col = curr_col + dy[itr]

                    if new_row >= 0 and new_row < nrows and new_col >= 0 and new_col < ncols and heights[new_row][new_col] >= heights[curr_row][curr_col] and not visited[new_row][new_col]:
                        queue.append((new_row, new_col))
                        visited[new_row][new_col] = True
                        ocean.add((new_row, new_col))
                
        for col in range(ncols):
            bfs(0, col, pacific)
        for row in range(nrows):
            bfs(row, 0, pacific)

        for col in range(ncols):
            bfs(nrows-1, col, atlantic)
        for row in range(nrows):
            bfs(row, ncols-1, atlantic)

        common = pacific & atlantic
        ans = []
        for elem in common:
            ans.append(list(elem))
        return ans
