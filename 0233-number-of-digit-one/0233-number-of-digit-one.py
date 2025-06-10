class Solution:
    def countDigitOne(self, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(pos, count, isLimit):
            if pos == 0:
                return count
            
            upper_bound = digits[pos] if isLimit else 9

            answer = 0
            for digit in range(upper_bound + 1):
                answer += dfs(pos-1, count+(digit==1), isLimit and digit == upper_bound)

            return answer
        
        digits = [0] * 11
        length = 0
        while n:
            digits[length+1] = n % 10
            n //= 10
            length += 1
        

        return dfs(length, 0, True)