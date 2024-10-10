class Solution:
    def myAtoi(self, s: str) -> int:
        cleaned_s = s.strip()

        if cleaned_s =="":
            return 0

        sign = 1
        if cleaned_s[0].isdigit():
            pass
        elif cleaned_s[0] == '+' or cleaned_s[0] == '-':
            if cleaned_s[0] == '-':
                sign = -1
            cleaned_s = cleaned_s[1:]
        else:
            return 0

        answer = 0
        for i in range(len(cleaned_s)):
            if not (cleaned_s[i].isdigit()):
                break

            answer = answer * 10 + int(cleaned_s[i])
        
        if answer * sign < -2**31:
            return -2**31
        elif answer * sign > 2**31-1:
            return 2**31-1

        return answer * sign