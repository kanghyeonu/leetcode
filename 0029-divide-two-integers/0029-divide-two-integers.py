class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        answer = 0
        sign = -1 if dividend * divisor < 0 else 1
        n, d = abs(dividend), abs(divisor)

        while n >= d:
            temp, q = d, 1
            while n >= temp:
                n -= temp
                answer += q
                temp <<= 1
                q <<= 1

        if sign * answer < -2**31:
            return -2**31
        elif sign * answer > 2**31 - 1:
            return 2**31 - 1

        return sign * answer