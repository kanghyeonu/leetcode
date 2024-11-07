class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        answer = [-1, -1]

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                answer = [m, m]
                break
            
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        if answer[0] > -1:
            while nums[answer[0]] == target:
                answer[0] -= 1
                if answer[0] == -1:
                    break
            answer[0] += 1 
            
            while nums[answer[1]] == target:
                answer[1] += 1
                if answer[1] == len(nums):
                    break
            answer[1] -= 1 

        return answer
            
