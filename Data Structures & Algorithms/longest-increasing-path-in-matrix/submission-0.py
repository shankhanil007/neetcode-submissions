class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        nrows = len(matrix)
        ncols = len(matrix[0])
        visited = set()
        ans = -float('inf')
        dp = [[1] * ncols for _ in range(nrows)]
        dx = [0, -1, 1, 0]
        dy = [-1, 0, 0, 1]


        def helper(row, col):
            nonlocal ans
            visited.add((row, col))

            for itr in range(4):
                new_row = row + dx[itr]
                new_col = col + dy[itr]
                if 0 <= new_row < nrows and 0 <= new_col < ncols and matrix[new_row][new_col] >  matrix[row][col]:
                    if (new_row, new_col) in visited:
                        dp[row][col] = max(dp[row][col], 1 + dp[new_row][new_col])
                    
                    else:
                        dp[row][col] = max(dp[row][col], 1 + helper(new_row,new_col))
                       
            ans = max(ans, dp[row][col])
            return dp[row][col]

        for i in range(nrows):
            for j in range(ncols):
                if (i, j) not in visited:
                    print(matrix[i][j])
                    helper(i, j)

        return ans