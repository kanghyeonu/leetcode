class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        buyPrices = [float('inf'), float('inf')]
        profits = [0, 0]
        for price in prices:
            buyPrices[0] = min(price, buyPrices[0])
            profits[0] = max(profits[0], price - buyPrices[0])
            buyPrices[1] = min(price - profits[0], buyPrices[1])
            profits[1] = max(profits[1], price - buyPrices[1])
        
        return profits[1]
    