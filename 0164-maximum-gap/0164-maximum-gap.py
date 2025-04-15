class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()

        gap = 0
        for i in range(1, len(nums)):
            temp = nums[i] - nums[i-1]
            if gap < temp:
                gap = temp

        return gap

        