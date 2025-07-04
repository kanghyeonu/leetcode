class Solution:
    def count_neighbors(self, i, j):
        count = 0
        # 상
        if 0 < i and self.board[i-1][j] == 1:
            count += 1
        # 하
        if self.m - 1 > i and self.board[i+1][j] == 1:
            count += 1
        # 좌
        if 0 < j and self.board[i][j-1] == 1:
            count += 1
        #우
        if self.n - 1 > j and self.board[i][j+1] == 1:
            count += 1
        
        # 우상
        if self.n - 1 > j and 0 < i and self.board[i-1][j+1] == 1:
            count += 1
        # 좌상
        if 0 < i and 0 < j and self.board[i-1][j-1] == 1:
            count += 1
        # 우하
        if self.m - 1 > i and self.n - 1 > j and self.board[i+1][j+1] == 1:
            count += 1
        # 좌하
        if self.m - 1 > i and 0 < j and self.board[i+1][j-1] == 1:
            count += 1

        return count

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        updated = [[0 for _ in range(self.n)] for _ in range(self.m)]

        def update_status(i, j, live):
            count = self.count_neighbors(i, j)

            if live and count < 2:
                return 0

            elif live and count == 2 or count == 3:
                return 1

            elif live and count > 3:
                return 0
             
            elif not live and count == 3:
                return 1
            
            return live

        for i in range(self.m):
            for j in range(self.n):
                updated[i][j] = update_status(i, j, board[i][j])
        
        for i in range(self.m):
            for j in range(self.n):
                board[i][j] = updated[i][j]
                    
            