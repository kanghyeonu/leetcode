class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if c < r:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in range(len(matrix)):
            matrix[r] = matrix[r][::-1]
