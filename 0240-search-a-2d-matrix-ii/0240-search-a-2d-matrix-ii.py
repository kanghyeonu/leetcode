class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        values = set()
        for i in range(m):
            if matrix[i][0] == target:
                return True

            elif matrix[i][0] < target:
                values.update(matrix[i])
            
            else:
                return False
            
            if target in values:
                return True
