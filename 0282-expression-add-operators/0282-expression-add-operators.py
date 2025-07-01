class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def dfs(idx, prev_operand, current_val, expression):
            if idx == len(num):
                if current_val == target:
                    res.append(expression)
                return
          

            for i in range(idx, len(num)):
                if i != idx and num[idx] == '0':
                    break
              
                current_operand = int(num[idx : i + 1])
              
                if idx == 0:
                    dfs(i + 1, current_operand, current_operand, str(current_operand))
                else:

                    dfs(i + 1, current_operand, current_val + current_operand, expression + "+" + str(current_operand))
                    dfs(i + 1, -current_operand, current_val - current_operand, expression + "-" + str(current_operand))

                    next_val =  current_val - prev_operand + (prev_operand * current_operand)  # 곱셈 우선 순위 역산
                    dfs(i + 1, prev_operand * current_operand, next_val, expression + "*" + str(current_operand))

        dfs(0, 0, 0, "")
        return res