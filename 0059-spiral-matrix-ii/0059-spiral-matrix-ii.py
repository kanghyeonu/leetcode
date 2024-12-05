class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer = [[0 for _ in range(n)] for _ in range(n)]
        check = [[False for _ in range(n)] for _ in range(n)]

        i, j = 0, 0
        cycle = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        c, num = 0, 1
        while num <= n*n:
            answer[i][j] = num
            check[i][j] = True

            i, j = i + cycle[c%4][0], j + cycle[c%4][1]
            if i >= n or i < 0 or j >= n or j < 0 or check[i][j]:
                i, j = i - cycle[c%4][0], j - cycle[c%4][1]
                c += 1
                i, j = i + cycle[c%4][0], j + cycle[c%4][1]
            num += 1

        return answer