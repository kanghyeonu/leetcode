class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        if "" in strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        i = 0
        prefix = strs[0][i]
        while 1:
            for j in range(len(strs)):
                if i == len(strs[j]):
                    return answer
                if prefix != strs[j][i]:
                    return answer

            answer += strs[0][i]
            
            if i < len(strs[0])-1:
                i += 1
                prefix = strs[0][i]
            else:
                break
        
        return answer
        