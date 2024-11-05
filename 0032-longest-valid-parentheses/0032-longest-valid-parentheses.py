from collections import deque
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        d = deque([-1])
        answer = 0

        for i in range(len(s)):
            if s[i] == '(':
                d.append(i)
            else:
                d.pop()
                if len(d) == 0:
                    d.append(i)
                else:
                    answer = max(answer, i-d[-1])
        return answer    