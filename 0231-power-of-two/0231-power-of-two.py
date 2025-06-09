class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        values = set([2**i for i in range(32)])
        return True if n in values else False


        