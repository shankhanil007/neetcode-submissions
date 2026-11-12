class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)

        dp = [[0]*n for _ in range(m)]
        
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue
                if obstacleGrid[row][col] != 1:
                    if row-1 >= 0:
                        dp[row][col] += dp[row-1][col] 
                    if col-1>=0:
                        dp[row][col] += dp[row][col-1]
                
        
        return dp[m-1][n-1]