class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s) + 1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]

