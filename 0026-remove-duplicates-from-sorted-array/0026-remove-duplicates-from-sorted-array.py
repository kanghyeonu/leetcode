class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s, i = 0, 1
        while i < len(nums):
            if nums[s] == nums[i]:
                i += 1
            else:
                nums[s + 1] = nums[i]
                s += 1
                i += 1

        return s + 1