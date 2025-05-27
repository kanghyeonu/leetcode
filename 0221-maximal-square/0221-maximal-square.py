class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)] 

        answer = 0
        for i in range(n):
            dp[0][i] = int(matrix[0][i])
            answer = max(dp[0][i], answer) 
            
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            answer = max(dp[i][0], answer) 
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    answer = max(answer, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return answer ** 2
