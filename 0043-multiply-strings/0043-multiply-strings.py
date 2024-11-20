class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        answer = 0
        result = []

        num1 = num1[::-1]
        num2 = num2[::-1]

        for n2 in num2:
            carry = 0
            digit = []
            for n1 in num1:
                curr = (int(n1) * int(n2)) + carry
                digit.append(curr%10)
                carry = curr // 10

            if carry != 0:
                digit.append(carry)
                
            sum_ = 0
            for i in range(len(digit)):
                sum_ += digit[i] * (10**i)

            result.append(sum_)

        for i in range(len(result)):
            curr = result[i] * (10**i)
            answer += curr

        return str(answer)