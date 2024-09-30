class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val1 in enumerate(nums):
            index1 = i
            for j, val2 in enumerate(nums):
                if i == j:
                    continue
                if target - val1 == val2:
                    return [i, j]