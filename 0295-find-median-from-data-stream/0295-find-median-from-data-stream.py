class MedianFinder:

    def __init__(self):
        self.values = []
        self.len = 0


    def addNum(self, num: int) -> None:
        self.values.append(num)
        self.len += 1
        

    def findMedian(self) -> float:
        self.values.sort()
        if self.len % 2 == 1:
            return self.values[self.len//2]
        
        idx = self.len // 2
        return (self.values[idx-1] + self.values[idx])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()