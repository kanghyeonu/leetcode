from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False
        @lru_cache(None)
        def dp(s_1, s_2):
            if s_1 == s_2:
                return True
            
            for i in range(1, len(s_1)):
                if dp(s_1[:i], s_2[:i]) and dp(s_1[i:], s_2[i:]):
                    return True
                if dp(s_1[:i], s_2[-i:]) and dp(s_1[i:], s_2[:-i]):
                    return True

            return False
        
        return dp(s1, s2)