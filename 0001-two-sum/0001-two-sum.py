class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in dic:
                return [dic[target - num], i] 
                
            dic[num] = i
            