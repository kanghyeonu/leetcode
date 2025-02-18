class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        answer = [[1] * i for i in range(1, numRows+1)]
        
        for i in range(2, numRows):
            for j in range(len(answer[i])):
                if j == 0 or j == len(answer[i]) - 1:
                    continue
                answer[i][j] = answer[i-1][j-1] + answer[i-1][j]

        return answer

