class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False

        mapping = defaultdict()
        seen = set()

        for p, w in zip(pattern, s):
            if p not in mapping and w not in seen:
                mapping[p] = w
                seen.add(w)
            
            if  p not in mapping and w in seen:
                return False

            elif p in mapping and mapping[p] != w:
                return False

            

        return True
