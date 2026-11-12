class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        nrows = len(heights)
        ncols = len(heights[0])
        

        def bfs(curr_row, curr_col, visited, ocean):
            queue = collections.deque()
            queue.append((curr_row, curr_col))
            visited.add((curr_row, curr_col))
            ocean.add((curr_row, curr_col))

            row_delta = [0, -1, 1, 0]
            col_delta = [-1, 0, 0, 1]

            while queue:
                top = queue.popleft()
                curr_row = top[0]
                curr_col = top[1]

                for itr in range(0, 4):
                    new_row = curr_row + row_delta[itr]
                    new_col = curr_col + col_delta[itr]

                    if new_row >= 0 and new_row < nrows and new_col >= 0 and new_col < ncols and heights[new_row][new_col] >= heights[curr_row][curr_col] and (new_row,new_col) not in visited:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
                        ocean.add((new_row, new_col))


        def dfs(curr_row, curr_col, visited, ocean):
            visited.add((curr_row, curr_col))
            ocean.add((curr_row, curr_col))

            row_delta = [0, -1, 1, 0]
            col_delta = [-1, 0, 0, 1]

            for itr in range(0, 4):
                new_row = curr_row + row_delta[itr]
                new_col = curr_col + col_delta[itr]

                if new_row >= 0 and new_row < nrows and new_col >= 0 and new_col < ncols and heights[new_row][new_col] >= heights[curr_row][curr_col] and (new_row,new_col) not in visited:
                    dfs(new_row, new_col, visited, ocean)

        visited = set()
        pacific = set()
        atlantic = set()

        for col in range(ncols):
            dfs(0, col, visited, pacific)
        for row in range(nrows):
            dfs(row, 0, visited, pacific)

        visited = set()
        for col in range(ncols):
            dfs(nrows-1, col, visited, atlantic)
        for row in range(nrows):
            dfs(row, ncols-1, visited, atlantic)
        
        common = pacific & atlantic
        ans = []
        for elem in common:
            ans.append(list(elem))
        return ans




