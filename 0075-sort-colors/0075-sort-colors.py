class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        m = 0

        while m <= r:
            # red
            if nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                l += 1
                m += 1
            
            # white
            elif nums[m] == 1:
                m += 1
            
            # blue
            else:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1