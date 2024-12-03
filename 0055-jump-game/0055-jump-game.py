class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[0] = True

        for i in range(len(nums)-1):
            if dp[i] == False:
                continue
            for j in range(1, nums[i]+1):
                if i + j > len(nums)-1:
                    return True
                
                dp[i+j] = True
                    
                
        return dp[-1]