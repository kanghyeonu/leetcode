class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []       

        def backtracking(start, p):
            if start == len(s):
                answer.append(p)
                return
            
            for end in range(start+1, len(s)+1):
                if s[start:end] == s[start:end][::-1]:
                    backtracking(end, p + [s[start:end]])
        
        backtracking(0, [])
        return answer