class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = int(len(nums)/3)
        counter = Counter(nums)
        answer = []
        for k, v in counter.items():
            if v > n:
                answer.append(k)
        
        return answer