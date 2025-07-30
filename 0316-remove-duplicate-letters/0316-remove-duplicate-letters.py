class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        # 초기화
        count = Counter(s)
        stack = [s[0]]
        count[s[0]] -= 1
        
        for i in range(1, len(s)):
            char = s[i]

            # 후순위 문자이면서 최초 등장한 문자라면
            if stack[-1] < char:
                if char not in stack:
                    stack.append(char)

            # 역순인 문자지만 이미 추가된 문자는 패스
            elif char in stack:
                pass

            # 역순 문자 - 현 문자보다 후순위인 중복 문자들은 스택내에서 제거
            else:
                # 뺄 수 없는 문자라면 패스
                if count[stack[-1]] == 0:
                    pass
                # 뺄 수 있는 문자라면 중복 및 후순위 문자를 일괄제거
                else:
                    while stack and count[stack[-1]] > 0 and stack[-1] >= char:
                        stack.pop()

                # 추가
                if char not in stack:
                    stack.append(char)

            count[char] -= 1
        
        return "".join(stack)