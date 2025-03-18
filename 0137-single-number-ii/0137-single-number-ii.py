class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        answer = [n for n, v in counter.items() if v == 1]
        return answer[0]