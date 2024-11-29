class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def findmaxSubArr(l, r):
            if l >= r:
                return nums[l]
            
            m = (l+r)//2

            lMax = findmaxSubArr(l, m)
            rMax = findmaxSubArr(m+1, r)
            crossMax = getMaxCross(l, m, r)

            return max(lMax, rMax, crossMax)
        
        def getMaxCross(l, m, r):
            lSum, lMax = 0, nums[m]
            for i in range(m, l-1, -1):
                lSum += nums[i]
                lMax = max(lSum, lMax)

            rSum, rMax = 0, nums[m+1]
            for i in range(m+1, r+1):
                rSum += nums[i]
                rMax = max(rMax, rSum)
            
            return max(lMax+rMax, lMax, rMax)

        return findmaxSubArr(0, len(nums)-1)