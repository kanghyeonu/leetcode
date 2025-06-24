class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)

        for n in range(len(seen)):
            if n not in seen:
                return n
        
        return len(seen)