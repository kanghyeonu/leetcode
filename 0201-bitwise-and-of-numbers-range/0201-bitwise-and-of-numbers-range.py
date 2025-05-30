class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left * 2 < right:
            return 0

        cnt = 0
        while (left != right):
            left >>= 1
            right >>= 1 
            cnt += 1        

        return left << cnt

