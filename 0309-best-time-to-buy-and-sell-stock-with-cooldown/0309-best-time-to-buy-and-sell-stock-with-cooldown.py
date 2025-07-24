class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        sell = 0
        prev_sell = 0
        buy = float('-inf')
        prev_buy = None

        for p in prices:
            prev_buy = buy # 현 시점 마지막 매수 값을 저장
            buy = max(prev_sell - p, prev_buy) # 이전 매도 값에서 지금 매수 이득 vs 이전에 매수 값
            prev_sell = sell # 현 시점 마지막 매도 값 저장
            sell = max(prev_buy + p, prev_sell) # 이전 매수 값에서 지금 매도 이득 vs 이전에 팔아서 쿨타임 상태

        return sell