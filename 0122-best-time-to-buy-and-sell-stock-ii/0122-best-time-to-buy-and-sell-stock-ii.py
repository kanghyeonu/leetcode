class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        buyPrice = -1
        sellPrice = 0
        buyReady = True
        for i in range(len(prices)):
            # 첫 시작 일단 사기
            if buyPrice == -1:
                buyPrice = prices[i]
                continue

            # 원래 샀던 가격보다 더 싸면 갱신
            if buyReady and buyPrice > prices[i]:
                buyPrice = prices[i]
            
            # 샀던 가격보다 비싸면
            if buyPrice < prices[i]:
                buyReady = False
                # 팔 가격 체크, 기존에 팔기로한 가격보다 크면 팔 가격 갱신
                if sellPrice <= prices[i]:
                    sellPrice = prices[i]

                    # 갱신 됐으나 마지막 값이면 매도
                    if i == len(prices)-1:
                        answer += sellPrice - buyPrice
                    
                    # 기존의 파는 가격보다 싸다면 매도하고 다시 매수
                    else:
                        answer += sellPrice - buyPrice
                        sellPrice = 0
                        buyPrice = prices[i]
                        buyReady = True
                
        return answer
