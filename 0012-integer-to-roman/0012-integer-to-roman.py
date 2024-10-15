class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I'
        }

        unit_values = [1000, 100, 10, 1]        

        answer = ""
        for val in unit_values:
            quot = num//val
            num = num%val

            if quot == 4 or quot == 9:
                if val >= 1000:
                    pass
                elif val >= 100:
                    answer += "CM" if quot == 9 else "CD"
                elif val >= 10:
                    answer += "XC" if quot == 9 else "XL"
                else:
                    answer += "IX" if quot == 9 else "IV"
            else:
                if quot == 0:
                    pass
                elif quot < 4:
                    for i in range(quot):
                        answer += symbols[val]
                elif quot == 5:
                    answer += symbols[quot*val]
                elif quot < 9:
                    answer += symbols[5*val]
                    for i in range(quot - 5):
                        answer += symbols[val]

        
        return answer