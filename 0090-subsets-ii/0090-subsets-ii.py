class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        
        def dfs(start, subSet):
            answer.append(subSet)

            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    continue
                
                dfs(i+1, subSet+[nums[i]])

        dfs(0, [])
        return answer
