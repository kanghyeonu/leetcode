class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0 for _ in range(cols)]
        answer = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            s = []
            for k in range(cols + 1):
                currH = 0 if k == cols else heights[k]
                while s and currH < heights[s[-1]]:
                    h = heights[s.pop()]
                    w = k if not s else k - s[-1] - 1
                    answer = max(answer, h * w)
                s.append(k)

        return answer