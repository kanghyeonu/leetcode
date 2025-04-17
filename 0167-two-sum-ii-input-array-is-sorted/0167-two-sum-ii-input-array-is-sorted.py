class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memo = defaultdict()
        memo[numbers[0]] = 0
        for i in range(1, len(numbers)):
            rest = target - numbers[i] 
            if rest in memo.keys():
                return [memo[rest]+1, i+1]
            
            memo[numbers[i]] = i
