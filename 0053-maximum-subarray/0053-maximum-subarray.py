class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        currSum = nums[0]

        for n in nums[1:]:
            currSum = max(n, currSum + n)
            answer = max(answer, currSum)
        
        return answer