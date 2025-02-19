class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        dp = [[float("inf")] * (i+1) for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        dp[1][0] = dp[0][0] +  triangle[1][0]
        dp[1][1] = dp[0][0] +  triangle[1][1]

        for i in range(2, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i-1][0]

                elif j == len(triangle[i])-1:
                    dp[i][j] = triangle[i][j] + dp[i-1][-1]
                    
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1])

        
        return min(dp[-1])
