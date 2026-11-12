class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ### For each cell 1 + sum of area from 4 sides 
        
        nrows = len(grid)
        ncols = len(grid[0])
        visited = set()

        def dfs(curr_row, curr_col, area):

            visited.add((curr_row, curr_col))
            # area = 0        #### 1 + sum of area from 4 sides 
            area += 1         #### Approach 2

            row_delta = [0, -1, 1, 0]
            col_delta = [-1, 0, 0, 1]

            for itr in range(0, 4):
                new_row = curr_row + row_delta[itr]
                new_col = curr_col + col_delta[itr]
                if new_row >= 0 and new_row < nrows and new_col >= 0 and new_col < ncols and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    # area += dfs(new_row, new_col)         #### 1 + sum of area from 4 sides 
                    area = dfs(new_row, new_col, area)      #### Approach 2
            
            # return 1 + area       #### 1 + sum of area from 4 sides
            return area             #### Approach 2 

        ans = 0

        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = dfs(i, j, 0)   ## For approach 1 we do not send the area. For #2 we send the area.
                    ans = max(ans, area)
                    
        return ans