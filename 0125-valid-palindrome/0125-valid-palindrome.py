class Solution:
    def isPalindrome(self, s: str) -> bool:
        onlyStr = "".join(s.strip().split())
        onlyAlpha = "".join(c for c in onlyStr if c.isalpha() or c.isnumeric())

        if onlyAlpha.lower() == onlyAlpha[::-1].lower():
            return True
        else:
            return False