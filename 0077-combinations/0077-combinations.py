class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        answer = []

        def dfs(combs, index):
            if len(combs) == k:
                answer.append(combs)
                return
            
            for i in range(index, len(nums)):
                dfs(combs + [nums[i]], i+1)

        dfs([], 0)

        return answer