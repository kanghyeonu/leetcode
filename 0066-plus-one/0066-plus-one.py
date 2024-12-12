class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] = digits[-1] + 1 

        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + carry
            carry = 0
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
            
            if carry == 0:
                break
            
        if carry > 0:
            digits = digits[::-1]
            digits.append(1)
            digits = digits[::-1]

        return digits