class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        operator = "+"
        stack = []

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            
            if i == len(s) - 1 or char in "+-*/":
                if operator == "+":
                    stack.append(num)

                elif operator == "-":
                    stack.append(-num)

                elif operator == "*":
                    stack.append(stack.pop() * num)

                elif operator == "/":
                    stack.append(int(stack.pop() / num))
                
                operator = char
                num = 0

        return sum(stack)


            