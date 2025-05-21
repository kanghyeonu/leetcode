class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if sum([i for i in range(1, k+1)]) > n:
            return []

        answer = []
        def dfs(num, path):
            if len(path) == k:
                if sum(path) == n:
                    answer.append(path)
                else:
                    return

            for i in range(num, 10):
                dfs(i+1, path + [i])
            

        dfs(1, [])
        return answer
