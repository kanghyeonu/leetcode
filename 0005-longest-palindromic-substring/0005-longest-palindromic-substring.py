import math
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        while l > 1:
            for i in range(len(s) - l + 1):
                target = s[i:i+l]

                for j in range(math.ceil(len(target)/2)):
                    if target[j] != target[(-1 * j) - 1]:
                        break
                    
                    if j == math.ceil(len(target)/2) - 1:
                        return target
            l -= 1
        return s[0]