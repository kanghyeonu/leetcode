class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) // 10 == 0:
            return x

        minus = ""
        if x < 0:
            minus = '-'
        
        s = list(str(abs(x)))
        s.reverse()

        while s[0] == '0':
            s = s[1:]
    
        answer = int(minus + "".join(s))

        if -2**31 < answer < 2**31 - 1:
            return answer
        else:
            return 0
