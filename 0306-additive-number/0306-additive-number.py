class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def is_valid(index, num1, num2):
            if index == len(num):
                return True
            
            sum_val = str(int(num1) + int(num2))
            if not num.startswith(sum_val, index):
                return False
            
            return is_valid(index + len(sum_val), num2, sum_val)

        for i in range(1, len(num) - 1):
            for j in range(i+1, len(num)):
                n1 = num[:i]
                if len(n1) > 1 and n1[0] == '0':
                    continue
                
                n2 = num[i : j]
                if len(n2) > 1 and n2[0] == '0':
                    continue
                
                if is_valid(j, n1, n2):
                    return True
        
        return False
                
