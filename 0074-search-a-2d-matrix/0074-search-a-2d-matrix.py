class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        targetRow = 0
        for r in range(row):
            if matrix[r][0] <= target and matrix[r][-1] >= target:
                targetRow = r
    
        l, r = 0, col-1
        while l <= r:
            m = (l+r)//2
            if matrix[targetRow][m] == target:
                return True
            if matrix[targetRow][m] < target:
                l = m + 1
            elif matrix[targetRow][m] > target:
                r = m - 1

        return False