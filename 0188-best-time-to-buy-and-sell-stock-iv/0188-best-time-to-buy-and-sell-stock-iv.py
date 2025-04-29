class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
      
        # dp 테이블 초기화
        # dp[남은 거래 횟수][주식 보유 유무] 
        # (주식 보유 유무 = 0) 주식을 들고 있지 않은 상태의 최대 이익
        # (주식 보유 유무 = 1) 주식을 들고 있는 상태에서 최대 이익
        profits = [[0] * 2 for _ in range(k + 1)]

        # dp 테이블 초기화
        # dp[j][0] = 주식 거래 자체를 안했으므로 0
        # dp[j][1] = 첫 날 주식을 샀으므로 음수처리
        for j in range(1, k + 1):
            profits[j][1] = -prices[0]
      
        # 첫날은 초기화 했으므로 그 다음 날부터 거래 시작
        for price in prices[1:]:
            # 가능한 거래 횟수에 따른 케이스 모두 계산 
            # k번, k-1, ... 1번 거래 
            for j in range(k, 0, -1):
                # 현 시점에서 주식을 들고 있지 않을 때 최대 이익 계산
                # max(현재 들고 있는걸 팔거나, 팔아버렸거나, 이전에 사지 않아서 대기하고 있거나)
                profits[j][0] = max(profits[j][1] + price, profits[j][0])
              
                # 현 시점 주식을 들고 있을 때의 최대 이익 계산
                # max(오늘 주식을 샀거나, 이전에 샀던걸 그대로 들고 있거나)
                profits[j][1] = max(profits[j - 1][0] - price, profits[j][1])
      
        # Return the maximum profit after the allowable number of transactions
        # without holding any stock
        return profits[k][0]