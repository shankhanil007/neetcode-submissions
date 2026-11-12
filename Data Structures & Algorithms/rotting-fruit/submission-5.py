class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        nrows = len(grid)
        ncols = len(grid[0])
        queue = collections.deque()
        dx = [0, -1, 1, 0]
        dy = [-1, 0, 0, 1]

        time = 0

        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 2:
                     queue.append((row, col, 0))

        while queue:
            top = queue.popleft()
            curr_row = top[0]
            curr_col = top[1]
            curr_time = top[2]
            time = max(curr_time, time)
            
            for itr in range(4):
                new_row = curr_row + dx[itr]
                new_col = curr_col + dy[itr]
                if 0 <= new_row < nrows and 0 <= new_col < ncols and grid[new_row][new_col] == 1 :
                    queue.append((new_row, new_col, curr_time + 1))
                    grid[new_row][new_col] = 2  ##### VVVIMMMPPP

        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 1:
                    return -1

        return time