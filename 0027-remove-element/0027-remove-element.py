class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s, i = 0, 0
        while i < len(nums):
            if nums[i] != val:
                nums[s] = nums[i]
                s += 1
            i += 1 
        

        return s