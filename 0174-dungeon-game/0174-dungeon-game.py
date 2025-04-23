class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # 공주 위치 부터 역순 -> 체력 조건만 고려하면 됨
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 양수 -> 체력 필요없음 -
                # 음수 -> 체력 필요함 +
                roomDamage = dungeon[i][j]

                # 항상 방에 도착했을 시 체력이 1 이상 있어야하므로 비교값이 음수라면 1로 전환
                # 공주 위치
                if i == m-1 and j == n-1:
                    dp[i][j] = max(1, 1 - roomDamage)
                    continue
                
                # 끝 행
                if i == m-1:
                    dp[i][j] = max(1, dp[i][j+1] - roomDamage)
                    continue
                
                # 끝 열
                if j == n-1:
                    dp[i][j] = max(1, dp[i+1][j] - roomDamage)
                    continue
                
                minHP = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, minHP - roomDamage)

        return dp[0][0]