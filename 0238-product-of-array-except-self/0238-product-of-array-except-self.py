class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total = 1
        index = 0
        cnt = 0
        for i, val in enumerate(nums):
            if val == 0:
                cnt += 1
                index = i
                continue

            total *= val
        answer = []
        if cnt > 1:
            answer = [0 for i in range(len(nums))]

        elif cnt == 1:
            answer = [0 for i in range(len(nums))]
            answer[index] = total

        else:
            for i in range(len(nums)):
                answer.append(int(total/nums[i]))

        return answer    