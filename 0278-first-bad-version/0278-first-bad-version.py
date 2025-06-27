# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while True:
            m = (l + r)//2
            if isBadVersion(m) and not isBadVersion(m-1):
                return m
            
            if isBadVersion(m):
                r = m - 1
            
            else:
                l = m + 1
