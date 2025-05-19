class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def doRop(houses):
            dp = [0] * (len(houses) + 1)
            dp[0] = 0
            dp[1] = houses[0]
            for i in range(2, len(houses)+1):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i-1])
            
            return dp[-1]
        
        answer1 = doRop(nums[1:])
        answer2 = doRop(nums[:-1])
        return max(answer1, answer2)