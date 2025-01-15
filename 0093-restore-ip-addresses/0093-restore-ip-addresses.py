class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []

        answer = []
        def dfs(idx, ip):
            if len(ip) > 4:
                return

            if idx == len(s) and len(ip) == 4 :
                answer.append(".".join(ip))
                return

            if idx < len(s) and s[idx] == "0":
                dfs(idx+1, ip + ["0"])
                return

            for l in range(1, 4):
                if idx + l > len(s):
                    return

                if 0 <= int(s[idx:idx+l]) <= 255:
                    dfs(idx+l, ip + [s[idx:idx+l]])


        dfs(0, [])
        return answer