class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = list(map(int, version1.split(".")))
        ver2 = list(map(int, version2.split(".")))

        if len(ver1) > len(ver2):
            for _ in range(len(ver1)-len(ver2)):
                ver2.append(0)
        elif len(ver1) < len(ver2):
            for _ in range(len(ver2)-len(ver1)):
                ver1.append(0)
            
        for v1, v2 in zip(ver1, ver2):
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        
        return 0

        