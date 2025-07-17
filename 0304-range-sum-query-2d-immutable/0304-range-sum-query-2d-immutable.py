class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_rows = []
        self.prefix_cols = []
        for rows in self.matrix:
            sums = 0
            prefix = []
            for n in rows:
                sums += n
                prefix.append(sums)
            
            self.prefix_rows.append(prefix)

        for i in range(len(self.matrix[0])):
            sums = 0
            prefix = []
            for j in range(len(self.matrix)):
                sums += matrix[j][i]
                prefix.append(sums)
            
            self.prefix_cols.append(prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if  row2 - row1 ==  col2 - col1 == 0:
            return self.matrix[row2][col2]
            
        elif row2 - row1 == 0:
            if col1 == 0:
                return self.prefix_rows[row1][col2]

            return self.prefix_rows[row1][col2] - self.prefix_rows[row1][col1 -1]
        
        elif col2 - col1 == 0:
            if row1 == 0:
                return self.prefix_cols[col1][row2]

            return self.prefix_cols[col1][row2] - self.prefix_cols[col1][row1 -1]

        # 작은쪽 순회
        if row2 - row1 > col2 - col1:
            sums = 0
            if row1 == 0:
                for i in range(col1, col2+1):
                    sums += self.prefix_cols[i][row2]
            else:
                for i in range(col1, col2+1):
                    sums += self.prefix_cols[i][row2] - self.prefix_cols[i][row1 - 1]
            return sums
        else:
            sums = 0
            if col1 == 0:
                for i in range(row1, row2+1):
                    sums += self.prefix_rows[i][col2]
            else:
                for i in range(row1, row2+1):
                    sums += self.prefix_rows[i][col2] - self.prefix_rows[i][col1 - 1]
            return sums

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)