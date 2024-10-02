class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedList = sorted(nums1 + nums2)
        
        if len(mergedList) % 2 == 0:
            pre = mergedList[len(mergedList)//2 - 1]
            post = mergedList[len(mergedList)//2]
            return (pre + post) / 2
        else:
            return mergedList[len(mergedList)//2]