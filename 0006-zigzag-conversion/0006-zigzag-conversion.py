class Solution:
    def convert(self, s: str, numRows: int) -> str:
        asc = list(range(numRows))
        des = list(range(numRows-2, 0, -1))
        seq = asc + des

        l = ["" for _ in range(numRows)]

        for i, char in enumerate(s):
            l[seq[i % len(seq)]] += char

        return "".join(l)
        