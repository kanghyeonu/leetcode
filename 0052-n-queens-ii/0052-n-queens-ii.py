class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        self.answer = 0

        def dfs(row, b):
            if row == n:
                self.answer += 1
                return
            
            for col in range(n):
                if promising(row, col, b):
                    b[row][col] = "Q"
                    dfs(row+1, b)
                    b[row][col] = "."
 
        def promising(row, col, b):
            curRow, i = row-1, 1
            while curRow >= 0:
                if b[curRow][col] == "Q": 
                    return False

                if col + i < n:
                    if b[curRow][col + i] == "Q":
                        return False

                if col - i >= 0:
                    if b[curRow][col - i] == "Q":
                        return False
                
                curRow -= 1
                i += 1
            
            return True

        dfs(0, [["." for _ in range(n)] for _ in range(n)])
        return self.answer






        