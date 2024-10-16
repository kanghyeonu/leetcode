import itertools as it
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums = sorted(nums)
        
        for i in range(len(nums)):
            target = nums[i]
            if i > 0 and target == nums[i-1]:
                continue

            dic = {}
            flag = set()
            for j in range(i+1, len(nums)):
                num = nums[j]
                if -(target + num) in flag:
                    continue
                elif -(target + num) in dic:
                    answer.append([target, num, -(target + num)])
                    flag.add(-(target + num))

                dic[num] = j

        return answer