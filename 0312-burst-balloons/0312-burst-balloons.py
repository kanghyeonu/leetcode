class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1] # 양끝에 1이 있으므로 0 ~ n+1
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]

        # 풍선을 하나 택해서 터뜨리는 과정을 역으로 계산
        # -> 어떤 풍선을 마지막에 터뜨렸는지 역산하여 최대값 찾음

        for length in range(2, n + 2):#  구간의 길이: 최초 길이 3 -> [1, 터뜨릴 풍선,1]
            for left in range(0, n + 2 - length): # 구간의 왼쪽 끝
                right = left + length # 구간의 오른쪽 끝
                for k in range(left + 1, right): # 구간에서 터뜨릴 풍선 인덱
                    dp[left][right] = max(
                        dp[left][right],
                        # left --- (범위 사이 풍선들) --- k --- (범위 사이 풍선들) ---right
                        # dp[left][k] = left ~ k 까지 얻은 최대 점수
                        # dp[k][right] = k ~ right 까지 얻은 최대 점수
                        dp[left][k] + dp[k][right] + nums[left] * nums[k] * nums[right]
                    )
        
        return dp[0][n+1]
