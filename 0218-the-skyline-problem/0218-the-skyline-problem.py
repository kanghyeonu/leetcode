class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.removals = []

    def insert(self, elem):
        heapq.heappush(self.pq, -elem)

    def getMax(self):
        return -self.pq[0]

    def remove(self, elem):
        if elem == -self.pq[0]:
            heapq.heappop(self.pq)
            while self.removals and self.pq[0] == self.removals[0]:
                heapq.heappop(self.pq)
                heapq.heappop(self.removals)

        else: # 삭제 예약
            heapq.heappush(self.removals, -elem)

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for x1, x2, h in buildings:
            points.append([x1, h, 0])
            points.append([x2, h, 1])
        
        def compare(p1, p2):
            if p1[0] != p2[0]: # 두 점 좌표 중 x 좌표가 작은게 좌측으로(오름차순)
                return p1[0] - p2[0]
            if p1[2] != p2[2]: # 두 점의 x좌표가 같다면 사각형 시작 좌표가 좌측으로 (오름차순)
                return p1[2] - p2[2]
            if p1[2] == 0: # 두 점의 x좌표도 같고 사각형의 종류(시작, 끝)도 같은데 그게 시작이라면 높은거 앞
                return -(p1[1] - p2[1])
            return p1[1] - p2[1] # 끝 사각형 좌표면 낮은게 앞

        points.sort(key=cmp_to_key(compare))

        answer = []
        pq = PriorityQueue()
        pq.insert(0)
        for x, h, isEnd in points:
            prev_max = pq.getMax()
            if not isEnd:
                pq.insert(h)
                if pq.getMax() != prev_max:
                    answer.append([x, h])

            else:
                pq.remove(h)
                if pq.getMax() != prev_max:
                    answer.append([x, pq.getMax()])

        return answer

