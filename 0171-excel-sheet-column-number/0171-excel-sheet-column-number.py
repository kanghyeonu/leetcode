class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if len(columnTitle) < 2:
            return ord(columnTitle) - 64
        
        answer = 0
        pos = 1
        for alpha in columnTitle[::-1]:
            num = ord(alpha) - 64
            answer += (num*pos)
            pos *= 26

        return answer