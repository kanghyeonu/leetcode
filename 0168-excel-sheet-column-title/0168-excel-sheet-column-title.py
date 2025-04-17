class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber < 27:
            return chr(columnNumber + 64)
        
        n = columnNumber
        answer = ""

        while n > 0:
            if n % 26 == 0:
                answer += 'Z'
                n //= 26
                n -= 1
            else:
                answer += chr(n % 26 + 64)
                n //= 26
        
        return answer[::-1]