class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        nrows = len(grid)
        ncols = len(grid[0])
        self.visited = [[0] * ncols for _ in range(nrows)]

        def dfs(curr_row, curr_col):

            self.visited[curr_row][curr_col] = 1

            row_delta = [0, -1, 1, 0]
            col_delta = [-1, 0, 0, 1]

            area = 0

            for itr in range(0, 4):
                new_row = curr_row + row_delta[itr]
                new_col = curr_col + col_delta[itr]
                if new_row >= 0 and new_row < nrows and new_col >= 0 and new_col < ncols and grid[new_row][new_col] == 1 and self.visited[new_row][new_col] == 0:
                    area += dfs(new_row, new_col)
            
            return 1 + area

        ans = 0

        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1 and self.visited[i][j] == 0:
                    area = dfs(i, j)
                    print(area)
                    ans = max(ans, area)
                    
        
        return ans