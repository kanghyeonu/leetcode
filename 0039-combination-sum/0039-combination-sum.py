class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def dfs(total, index, candidate):
            if total > target:
                return
            if total == target:
                answer.append(candidate)
                return
            
            for i in range (index, len(candidates)):
                dfs(total + candidates[i], i, candidate + [candidates[i]])
            
        dfs(0, 0, [])
        return answer