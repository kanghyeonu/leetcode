class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        temp = [nums[0]]
        for i in range(1, len(nums)):
            if temp[-1] == nums[i]-1:
                temp.append(nums[i])
            
            else:
                ranges.append(temp)
                temp = [nums[i]]

        answer = []    
        ranges.append(temp)
        for r in ranges:
            if len(r) == 1:
                answer.append(f"{r[0]}")

            else:
                answer.append(f"{r[0]}->{r[-1]}")
        
        return answer



