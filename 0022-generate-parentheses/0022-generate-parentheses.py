from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def isValid(s):
            d = deque()
            for c in s:
                if c == "(":
                    d.append(c)
                    continue
                else:
                    if len(d) == 0: return False
                    opening = d.pop()
        
            if len(d) == 0:
                return True
            else:
                return False

        def dfs (p, opening, closing):
            if opening == closing == 0:
                if isValid(p):
                    answer.append(p)
                return

            if opening > 0:
                dfs(p+"(", opening-1, closing)
            if closing > 0:
                dfs(p+")", opening, closing-1)

        dfs("", n, n)
        return answer
