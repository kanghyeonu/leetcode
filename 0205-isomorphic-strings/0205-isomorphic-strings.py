class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapping = dict()
        for sc, tc in zip(s, t):
            
            if sc in mapping:
                # 매핑됐는데 값이 다르면 틀림
                if mapping[sc] != tc:
                    return False

            # 매핑시킬 값이 이미 사용된 경우
            elif tc in mapping.values():
                return False
            
            else:
                mapping[sc] = tc
            
        return True
