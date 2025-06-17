class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        hq = [-i for i in nums[:k]]
        heapq.heapify(hq)
        removals = []
        answer = [-hq[0]]

        for i in range(1, len(nums) - k + 1):
            if nums[i-1] == -hq[0]:
                heapq.heappop(hq)
                while removals and hq[0] == removals[0]:
                    heapq.heappop(hq)
                    heapq.heappop(removals)
            
            else:
                heapq.heappush(removals, -nums[i-1])
            
            heapq.heappush(hq, -nums[i+k-1])
            answer.append(-hq[0])

        return answer
            