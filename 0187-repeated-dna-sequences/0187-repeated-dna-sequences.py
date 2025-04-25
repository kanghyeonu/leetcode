class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = defaultdict(int)
        answer = set()
        for i in range(len(s) - 9):
            seq = s[i : i + 10]
            sequences[seq] += 1
            if sequences[seq] > 1:
                answer.add(seq)
        
        return list(answer)
