class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sLen = len(s)
        memo = [False] * (sLen + 1)
        memo[sLen] = True

        for i in range(sLen-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= sLen and s[i:i + len(w)] == w:
                    memo[i] = memo[i + len(w)]
                
                if memo[i]:
                    break
        print(memo)
        return memo[0]