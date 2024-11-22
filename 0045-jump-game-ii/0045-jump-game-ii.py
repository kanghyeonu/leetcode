class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]

        for i in range(len(nums)-1):
            for j in range(nums[i]+1):
                if i + j > len(nums)-1 or j == 0:
                    continue
                if dp[i+j] == 0:
                    dp[i+j] = dp[i] + 1
                elif dp[i+j] > dp[i] + 1:
                    dp[i+j] = dp[i] + 1
                
        return dp[-1]