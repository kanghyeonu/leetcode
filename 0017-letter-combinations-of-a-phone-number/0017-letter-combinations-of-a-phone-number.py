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
        def dfs(i, comb):
            if len(digits) == i:
                answer.append(comb)
                return
            

            for char in letters[digits[i]]:
                dfs(i+1, comb + char)

        dfs(0, "")

        return answer