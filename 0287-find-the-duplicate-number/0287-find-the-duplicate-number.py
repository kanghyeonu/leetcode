class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)

        for i, v in counter.items():
            if v > 1:
                return i