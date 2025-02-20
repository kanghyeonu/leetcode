class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if minPrice >= prices[i]:
                minPrice = prices[i]
                continue
            
            answer = max(answer, prices[i] - minPrice)

        return answer