class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]

        for i in range(len(nums)-1):
            for j in range(1, nums[i]+1):
                if i + j > len(nums)-1:
                    continue
                if dp[i+j] == 0:
                    dp[i+j] = dp[i] + 1
                
        return dp[-1]