class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        check = [[False for _ in range(col)] for _ in range(row)]
        answer = []
        i, j = 0, 0
        cycle = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        c = 0
        while len(answer) < row * col:
            answer.append(matrix[i][j])
            check[i][j] = True

            i, j = i + cycle[c%4][0], j + cycle[c%4][1]
            if i >= row or i < 0 or j >= col or j < 0 or check[i][j]:
                i, j = i - cycle[c%4][0], j - cycle[c%4][1]
                c += 1
                i, j = i + cycle[c%4][0], j + cycle[c%4][1]

        return answer