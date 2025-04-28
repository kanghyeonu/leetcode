class Solution:
    def reverseBits(self, n: int) -> int:
        original_n = format(n, 'b')
        zeros = "0" * (32 - len(original_n)) # add padding
        bin_n = format(n, 'b')[::-1] + zeros
        return int(bin_n, 2)