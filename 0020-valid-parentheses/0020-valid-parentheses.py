from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()
        characters = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in characters.keys():
                d.append(c)
                continue
            else:
                if len(d) == 0: return False
                opening = d.pop()
                closing = characters[opening]
                if closing != c: return False
    
        if len(d) == 0:
            return True
        else:
            return False