class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        s.reverse()
        return " ".join(s)