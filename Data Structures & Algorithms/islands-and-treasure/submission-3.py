class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        nrows = len(grid)
        ncols = len(grid[0])
        queue = collections.deque()
        dx = [0, -1, 1, 0]
        dy = [-1, 0, 0, 1]

        #### MISTAKE: Not starting the BFS together from all the 0s. The waves need to begin from all 0s at the same time.

        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 0:
                     queue.append((row, col, 0))

        while queue:
            top = queue.popleft()
            curr_row = top[0]
            curr_col = top[1]
            curr_distance = top[2]
            grid[curr_row][curr_col] = curr_distance
            
            for itr in range(4):
                new_row = curr_row + dx[itr]
                new_col = curr_col + dy[itr]
                if 0 <= new_row < nrows and 0 <= new_col < ncols and grid[new_row][new_col] == 2147483647 :
                    queue.append((new_row, new_col, curr_distance + 1))
                    grid[new_row][new_col] = 1

        return