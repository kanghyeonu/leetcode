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
            for j in range(i+1, len(nums)):
                num = nums[j]
                if -(target + num) in dic and dic[-(target + num)] == False:
                    answer.append([target, num, -(target + num)])
                    dic[-(target + num)] = True

                elif -(target + num) not in dic:
                    dic[num] = False
                    
                else:
                    continue
                    

        return answer