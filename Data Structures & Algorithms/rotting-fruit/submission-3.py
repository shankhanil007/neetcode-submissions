class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        nrows = len(grid)
        ncols = len(grid[0])

        queue = collections.deque()
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
        
        time  = 0
        row_delta = [0, -1, 1, 0]
        col_delta = [-1, 0, 0, 1]

        while queue:
            top = queue.popleft()
            curr_row = top[0]
            curr_col = top[1]
            curr_time = top[2]
            time = max(curr_time, time)

            for itr in range(0, 4):
                new_row = curr_row + row_delta[itr]
                new_col = curr_col + col_delta[itr]

                if new_row >= 0 and new_row < nrows and new_col >= 0 and new_col < ncols and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col, curr_time+1))

        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1:
                    return -1

        return time