class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def findIslands(r, c):
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr > m-1 or nc < 0 or nc > n-1:
                    continue
                findIslands(nr, nc)
                
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    findIslands(i, j)
                    answer += 1

        return answer 