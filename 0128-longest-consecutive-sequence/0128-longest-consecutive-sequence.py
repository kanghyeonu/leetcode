class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        prev = nums[0]
        answer = 0
        seqLen = 1
        for i in range(1, len(nums)):
            if nums[i] == prev:
                continue
            elif nums[i] - prev == 1:
                seqLen += 1
                prev = nums[i]
            else:
                answer = max(answer, seqLen)
                prev = nums[i]
                seqLen = 1
        
        return max(answer, seqLen)
            
