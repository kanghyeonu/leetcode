class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        l = list(str(x))

        for i in range(len(l)//2):
            if l[i] != l[-1*i - 1]:
                return False
        
        return True
