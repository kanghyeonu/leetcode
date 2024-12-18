class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        pos = []
        rowMark, colMark = set(), set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    pos.append((i, j))
        
        for i, j in pos:
            if i not in rowMark:
                rowMark.add(i)
                for c in range(col):
                    matrix[i][c] = 0

            if j not in colMark: 
                colMark.add(j)
                for r in range(row):
                    matrix[r][j] = 0
