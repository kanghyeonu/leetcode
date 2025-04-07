class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
            
        global answer
        answer = 0
        def findLine(p1):
            global answer
            lines = defaultdict(list)
            for p2 in points:
                if p1 == p2:
                    continue

                x1, x2 = p1[0], p2[0]
                y1, y2 = p1[1], p2[1]

                if x1 - x2 == 0:
                    lines['v'].append(p2)
                else:
                    slope = (y1 - y2) / (x1 - x2)
                    lines[slope].append(p2)

            answer = max(answer, len(max(lines.values(), key=len))+1)


        for p in points:
            findLine(p)
            
        return answer

