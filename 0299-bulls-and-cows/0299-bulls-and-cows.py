class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        seen = defaultdict(int)
        check = []
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            
            else:
                seen[s] += 1
                check.append(g)

        for g in check:
            if seen[g] > 0:
                cows += 1
                seen[g] -= 1

        return f"{bulls}A{cows}B"
            
            
