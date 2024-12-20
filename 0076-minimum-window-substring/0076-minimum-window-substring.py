class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        missing = len(t)
        need = collections.Counter(t)
        l = start = end = 0

        for r, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            if missing == 0:
                while l < r and need[s[l]] < 0:
                    need[s[l]] += 1
                    l += 1
                
                if not end or r - l <= end -start:
                    start, end = l, r
                
                need[s[l]] += 1
                missing += 1
                l += 1
        return s[start:end]
