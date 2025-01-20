class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3) or Counter(s1) + Counter(s2) != Counter(s3):
            return False

        stack, visited = [(0, 0)], set((0, 0))
        while stack:
            pos1, pos2 = stack.pop()
            if pos1 + pos2 == len(s3):
                return True
            if pos1 < len(s1) and s1[pos1] == s3[pos1 + pos2] and (pos1 + 1, pos2) not in visited:
                stack.append((pos1 + 1, pos2))
                visited.add((pos1 + 1, pos2))
            if pos2 < len(s2) and s2[pos2] == s3[pos1 + pos2] and (pos1, pos2 + 1) not in visited:
                stack.append((pos1, pos2 + 1))
                visited.add((pos1, pos2 + 1))
        return False