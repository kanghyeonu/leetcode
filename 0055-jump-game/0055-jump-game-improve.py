class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReachable = 0
        for i, jump in enumerate(nums):
            if i > maxReachable:
                return False

            maxReachable = max(maxReachable, i + jump)
            if maxReachable >= len(nums) - 1:
                return True
            
        return False