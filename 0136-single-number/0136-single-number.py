class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        answer = [n for n, cnt in counter.items() if cnt == 1]
        return answer[0]