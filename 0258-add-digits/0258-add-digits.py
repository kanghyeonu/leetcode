class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        answer = num
        while answer >= 10:
            value = answer
            answer = 0
            while value >= 10:
                answer += value % 10
                value //= 10
            answer += value
        
        return answer
            