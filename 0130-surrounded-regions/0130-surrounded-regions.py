class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        self.m, self.n = len(board), len(board[0])

        def bfs(r, c):
            dq = deque([(r, c)])
            board[r][c] = 'E' 

            while dq:
                sr, sc = dq.popleft()
                
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = sr + dr, sc + dc
                    if 0 <= nr < self.m and 0 <= nc < self.n and board[nr][nc] == 'O':
                        board[nr][nc] = 'E'
                        dq.append((nr, nc))

        for i in range(self.m):
            for j in range(self.n):
                if (i == 0 or i == self.m - 1 or j == 0 or j == self.n - 1) and board[i][j] == 'O':
                    bfs(i, j)

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'
                
