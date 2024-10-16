class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        if "" in strs:
            return ""

        def LCP(l, r):
            min_len = min(len(l), len(r))
            for i in range(min_len):
                if l[i] != r[i]:
                    return l[:i]
            return l[:min_len]

        def sol(strs, l, r):
            if l == r:
                return strs[l]
            else:
                mid = (l+r)//2
                LCP_l = sol(strs, l, mid)
                LCP_r = sol(strs, mid+1, r)
                return LCP(LCP_l, LCP_r)
        
        return sol(strs, 0, len(strs)-1)