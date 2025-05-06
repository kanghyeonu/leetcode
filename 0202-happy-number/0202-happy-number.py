class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        happy = n
        while happy != 1:
            if happy in seen:
                return False
            
            seen.add(happy)

            happy_str = str(happy)
            happy = 0
            for i in happy_str:
                happy += int(i)**2
            
        return True