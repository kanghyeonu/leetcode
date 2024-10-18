class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        answer = []
        def dfs(target, i, comb):
            if len(target) == i:
                answer.append(comb)
                return
            

            for char in letters[digits[i]]:
                dfs(target, i+1, comb + char)

        dfs(digits, 0, "")

        return answer