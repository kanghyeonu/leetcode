class Solution:
    def minCut(self, s: str) -> int:
        dp = [0] * len(s)

        for i in range(len(s)):
            min_cut = i
            for j in range(i+1):
                if s[j:i+1] == s[j:i+1][::-1]:
                    if j == 0:
                        min_cut = 0
                        break;
                        
                    min_cut = min(min_cut, dp[j - 1] + 1) # if j == 0 -> s[0:i+1] is Palindrome, don't need to cut -> min_cut = 0

            dp[i] = min_cut

        return dp[-1]
        