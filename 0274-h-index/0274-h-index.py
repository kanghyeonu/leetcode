class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort(reverse=True)
        
        for i, val in enumerate(citations):
            if i+1 > val:
                return i
        
        return len(citations)
