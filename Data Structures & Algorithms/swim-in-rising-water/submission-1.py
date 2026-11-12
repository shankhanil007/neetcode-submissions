class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        nrows = len(grid)
        ncols = len(grid[0])

        min_heap = []
        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        visited = set()

        dx = [0, -1, 1, 0]
        dy = [-1, 0, 0, 1]

        while min_heap:
            val, row, col = heapq.heappop(min_heap)
            
            if (row, col) in visited:
                continue

            visited.add((row, col))

            if row == nrows-1 and col == ncols-1:
                return val
            
            for itr in range(4):
                new_row = row + dx[itr]
                new_col = col + dy[itr]

                if 0 <= new_row < nrows and 0 <= new_col < ncols and (new_row, new_col) not in visited:
                    new_val = max(val, grid[new_row][new_col])
                    heapq.heappush(min_heap, (new_val, new_row, new_col))

        return -1


