class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def promising(row, col, num):
            for i in range(9):
                if board[i][col] == num or board[row][i] == num:  
                    return False
            for r in range(3*(row//3), 3*(row//3) + 3):
                for c in range(3*(col//3), 3*(col//3) + 3):
                    if board[r][c] == num:
                        return False
            return True

        def dfs(row, col):
            if row == 9:
                return True
            if col == 9:
                return dfs(row+1, 0)
            
            if board[row][col] != ".":
                return dfs(row, col+1)

            for num in range(1, 10):
                num_str = str(num)
                if promising(row, col, num_str):
                    board[row][col] = num_str 
                    if dfs(row, col+1):
                        return True
                    board[row][col] = "." 
            return False
            
        dfs(0, 0)