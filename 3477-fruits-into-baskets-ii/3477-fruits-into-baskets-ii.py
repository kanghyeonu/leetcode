class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        check = set()
        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if basket >= fruit and i not in check:
                    check.add(i)
                    break
        
        return len(fruits) - len(check)