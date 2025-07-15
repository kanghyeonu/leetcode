class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [nums[0]]
        for i in range(1, len(nums)):
            if lis[-1] < nums[i]:
                lis.append(nums[i])

            else:
                idx = bisect.bisect_left(lis, nums[i])
                lis[idx] = nums[i]
            
        return len(lis)