class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

        dp[1][1] = 0 if obstacleGrid[0][0] == 1 else 1

        for i in range(1, row+1):
            for j in range(1, col+1):
                if i == 1 and j == 1:
                    continue
                elif obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[-1][-1]
