class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        answer = list(itertools.permutations([n for n in range(1, n+1)]))
        return "".join(str(c) for c in answer[k-1])
        