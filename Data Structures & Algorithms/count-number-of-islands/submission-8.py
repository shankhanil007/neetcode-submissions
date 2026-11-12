class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        nrows = len(grid)
        ncols = len(grid[0])

        queue = collections.deque()
        visited = [[False] * ncols for _ in range(nrows)]

        def bfs(curr_row, curr_col):

            queue.append((curr_row, curr_col))
            visited[curr_row][curr_col] = True  

            dx = [0, -1, 1, 0]
            dy = [-1, 0, 0, 1]
             
            while queue:
                top = queue.popleft()
                row = top[0]
                col = top[1]

                for i in range(4):
                    new_row = row + dx[i]
                    new_col = col + dy[i]
                    if 0 <= new_row < nrows and 0 <= new_col < ncols and not visited[new_row][new_col] and grid[new_row][new_col] == "1":
                        queue.append((new_row, new_col))
                        visited[new_row][new_col] = True  

            return

        ans = 0
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == "1" and not visited[row][col]:
                    ans += 1
                    bfs(row, col)

        return ans



