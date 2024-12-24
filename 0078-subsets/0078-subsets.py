class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def dfs(index, sets):
            answer.append(sets)

            for i in range(index, len(nums)):
                dfs(i+1, sets + [nums[i]])

        dfs(0, [])
        return answer
