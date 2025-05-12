class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        s, sums = 0, 0
        answer = float('inf')

        for e, n in enumerate(nums):
            sums += n
            while sums >= target:
                answer = min(answer, e - s + 1)
                sums -= nums[s]
                s += 1

        return answer