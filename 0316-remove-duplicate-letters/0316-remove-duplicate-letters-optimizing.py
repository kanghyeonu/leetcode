class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        # 초기화
        count = Counter(s)
        stack = []
        in_stack = set()
        
        for char in s:
            count[char] -= 1

            # 사용된 문자라면 패스
            if char in in_stack:
                continue
            
            # 사전 역순 문자를 제거(불가능할 때 까지)
            while stack and char < stack[-1] and count[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)
            
            stack.append(char)
            in_stack.add(char)
            
        
        return "".join(stack)