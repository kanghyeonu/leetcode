class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(t):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < t:
                    l = m + 1
                else:
                    r = m - 1
            return l
        
        answer_l = bs(target)
        answer_r = bs(target + 1) - 1

        if answer_l <= answer_r:
            return [answer_l, answer_r]

        return [-1, -1]
            
