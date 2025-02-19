class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [[1] * (i+1) for i in range(rowIndex+1)]

        for i in range(2, rowIndex+1):
            for j in range(len(answer[i])):
                if j == 0 or j == len(answer[i])-1:
                    continue
                
                answer[i][j] = answer[i-1][j-1] + answer[i-1][j]

        return answer[rowIndex]