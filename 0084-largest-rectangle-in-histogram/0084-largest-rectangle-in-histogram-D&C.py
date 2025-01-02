class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def solve(l, r):
            if l == r:
                return heights[l]
            
            m = (l + r)//2
            maxArea = max(solve(l, m), solve(m + 1, r))

            Lside, Rside = m, m + 1
            minHeight = inf
            while l <= Lside and Rside <= r:
                minHeight = min(minHeight, heights[Lside], heights[Rside])
                maxArea = max(maxArea, (Rside - Lside + 1) * minHeight)
                if l == Lside:
                    Rside += 1
                elif r == Rside:
                    Lside -= 1
                elif heights[Lside - 1] <= heights[Rside + 1]:
                    Rside += 1
                else:
                    Lside -= 1
            
            return maxArea

        return solve(0, len(heights)-1)



            
           



