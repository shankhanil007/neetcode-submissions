class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0

        for row in range(m):
            for col in range(n):
                if (row != 0 or col != 0):
                    if obstacleGrid[row][col] != 1:
                        if 0<=(row-1)<m:
                            dp[row][col] += dp[row-1][col]
                        if 0<=(col-1)<n:
                            dp[row][col] += dp[row][col-1]
                    else:
                        dp[row][col] = 0


        return dp[m-1][n-1]