from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for p in list(permutations(nums)):
            answer.append(list(p))
        
        return answer
        
