class Solution:
    def simplifyPath(self, path: str) -> str:
        dq = collections.deque()
        path = [path for path in path.split("/") if path]

        for p in path:
            if p == ".":
                pass
            elif p == "..":
                print(dq)
                if len(dq) >= 1:
                    dq.pop()
                continue
            else:
                dq.append(p)

        return "/" + "/".join(dq)