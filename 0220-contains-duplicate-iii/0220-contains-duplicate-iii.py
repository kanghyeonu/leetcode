class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        sorted_set = SortedSet()

        for i, num in enumerate(nums):

            leftIndex = sorted_set.bisect_left(num - valueDiff)

            if leftIndex < len(sorted_set) and sorted_set[leftIndex] <= num + valueDiff:
                return True
            
            sorted_set.add(num)

            if len(sorted_set) > indexDiff:
                sorted_set.remove(nums[i - indexDiff])
        
        return False