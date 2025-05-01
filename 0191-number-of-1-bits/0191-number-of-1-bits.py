class Solution:
    def hammingWeight(self, n: int) -> int:
        return Counter(format(n, 'b'))['1']