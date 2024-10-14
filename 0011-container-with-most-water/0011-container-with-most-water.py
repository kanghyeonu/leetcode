class Solution:
    def maxArea(self, height: List[int]) -> int:

        def getArea(p1, p2) -> int:
            h = p1[1] if p1[1] < p2[1] else p2[1]
            l = abs(p1[0] - p2[0])
            return h * l
            
        l = 0
        r = len(height) -1
        answer = 0

        while l < r:
            answer = max(getArea([l, height[l]], [r, height[r]]), answer)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                    
        return answer