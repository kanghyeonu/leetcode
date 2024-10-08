class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        
        answer, x = 0, abs(x)
        
        while x:
            mod = x % 10
            x = x // 10
            answer = answer * 10 + mod

        if -2**31 < sign * answer < 2**31 - 1:
            return sign * answer
        else:
            return 0
