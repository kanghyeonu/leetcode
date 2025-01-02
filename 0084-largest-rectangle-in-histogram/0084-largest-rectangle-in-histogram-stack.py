class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [(-1, -1)]
        heights.append(0)
        answer = 0

        for i, h in enumerate(heights):
            if h >= s[-1][1]:
                s.append((i, h))
            else:
                while s[-1][1] > h:
                    temp_i, temp_h = s.pop()
                    answer = max(answer, (i - s[-1][0]-1)*temp_h)
                s.append((i, h))

        return answer



            
           



