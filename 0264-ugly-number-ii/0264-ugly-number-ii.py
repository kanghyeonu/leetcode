class Solution:
    def nthUglyNumber(self, n: int) -> int:
        answer = [0 for _ in range(n+1)]
        exp2, exp3, exp5 = 1, 1, 1
        answer[1] = 1

        for i in range(2, n+1):
            answer[i] = min(answer[exp2]*2, answer[exp3]*3, answer[exp5]*5)

            if answer[i] == answer[exp2]*2:
                exp2 += 1
            if answer[i] == answer[exp3]*3:
                exp3 += 1
            if answer[i] == answer[exp5]*5:
                exp5 += 1
        
        return answer[-1]




