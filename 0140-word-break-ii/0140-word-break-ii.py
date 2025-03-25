class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        memo = dict()
        def dfs(s):
            if s in memo:
                return memo[s]
            if not s: 
                return []
            
            result = []
            if len(s) == 0:
                result.append("")
                return result
            
            for word in wordDict:
                if not s.startswith(word):
                    continue
                
                if len(word) == len(s):
                    result.append(word)
                
                else:
                    sub = s[len(word):]
                    subString = dfs(sub)

                    for subStr in subString:
                        result.append(word + " " + subStr)
            
            memo[s] = result
            return result

        return dfs(s)