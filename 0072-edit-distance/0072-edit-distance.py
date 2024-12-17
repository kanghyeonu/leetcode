class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row = len(word2)
        col = len(word1)
        dp = [[0 for _ in range(col+1)] for _ in range(row+1)]

        for i in range(row+1):
            dp[i][0] = i

        for i in range(col+1):
            dp[0][i] = i
        
        for i in range(1, row+1):
            for j in range(1, col+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        return dp[-1][-1]