class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        def dfs(total, index, candidate):
            if total == target: 
                answer.append(candidate)
                return
            if total > target:
                return
            
            for i in range(index + 1, len(candidates)):
                if i - index > 1 and candidates[i] == candidates[i-1]:
                    continue
                dfs(total + candidates[i], i, candidate + [candidates[i]])
            
        dfs(0, -1, [])
        return answer