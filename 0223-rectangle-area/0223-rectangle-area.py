class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        def getRectArea(x1, x2, y1, y2):
            return abs(x2 - x1) * abs(y2 - y1)

        rect1 = getRectArea(ax1, ax2, ay1, ay2)
        rect2 = getRectArea(bx1, bx2, by1, by2)
        overlap_x = min(ax2, bx2) - max(ax1, bx1)
        overlap_y = min(ay2, by2) - max(ay1, by1)


        return rect1 + rect2 - (max(overlap_x, 0) * max(overlap_y, 0))

