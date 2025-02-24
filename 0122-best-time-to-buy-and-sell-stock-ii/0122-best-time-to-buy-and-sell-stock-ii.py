class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        answer = []
        buyPrice = prices[0]
        sellPrice = 0
        buyReady = True
        for i in range(1, len(prices)):
            if buyReady and buyPrice >= prices[i]:  
                buyPrice = prices[i]
            
            else:
                buyReady = False

                if sellPrice <= prices[i]:
                    sellPrice = prices[i]

                else:
                    answer.append(sellPrice - buyPrice)
                    buyReady = True
                    buyPrice = prices[i]
                    sellPrice = 0
            
            if i == len(prices)-1 and sellPrice > 0:
                answer.append(sellPrice - buyPrice)

        if not answer:
            return 0

        return sum(answer)
        


                
                