class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        exception = ['CM', 'CD', 'XL', 'XC', 'IV', "IX"]
        answer = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in exception:
                answer += (symbols[s[i+1]] - symbols[s[i]])
                i += 2
            else:
                answer += symbols[s[i]]
                i += 1
        
        return answer