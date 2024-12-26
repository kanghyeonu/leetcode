class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board[0]) # col
        m = len(board) # row

        def dfs(row, col, i):
            if i == len(word):
                return True
            
            if row >= m or row < 0 or col >= n or col < 0 or board[row][col] != word[i]:
                return False

            temp = board[row][col]
            board[row][col] = "#"

            found = (dfs(row+1, col, i+1) or
                    dfs(row-1, col, i+1) or
                    dfs(row, col+1, i+1) or
                    dfs(row, col-1, i+1))

            board[row][col] = temp
            return found

        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    if dfs(i, j, 0):
                        return True
            
        return False