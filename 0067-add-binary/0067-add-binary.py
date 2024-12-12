class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = int(a, 2) + int(b, 2)
        return format(answer, 'b')