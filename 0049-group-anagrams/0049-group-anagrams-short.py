class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        d = defaultdict(list)
        for s in strs:
            sorted_s = str(sorted(s))
            d[sorted_s].append(s)

        return list(d.values())