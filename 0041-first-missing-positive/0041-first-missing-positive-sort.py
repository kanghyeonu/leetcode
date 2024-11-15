class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        answer = 1
        nums.sort()
        for i in range(len(nums)):
            if nums[i] <= 0:
                continue
            
            if answer == nums[i]:
                answer += 1
            elif answer > nums[i] and nums[i] != nums[i-1]:
                break
        
        return answer
               
            