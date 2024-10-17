class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        answer = sum(nums[:3])

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                temp = nums[i] + nums[l] + nums[r]

                if temp < target:
                    l += 1
                elif temp > target:
                    r -= 1
                else:
                    return temp
                
                if abs(target - temp) < abs(target - answer):
                    answer = temp

        return answer