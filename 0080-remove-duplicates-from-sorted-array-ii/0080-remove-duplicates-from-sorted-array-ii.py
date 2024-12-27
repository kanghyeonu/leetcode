class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr, cnt = 1, 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                cnt = 1
            else:
                cnt += 1

            if cnt <= 2:
                if nums[i] != nums[curr]:
                    nums[curr] = nums[i]
                
                curr += 1
        
        return curr